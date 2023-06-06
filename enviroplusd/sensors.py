from bme280 import BME280
from ltr559 import LTR559
from enviroplus import gas
from pms5003 import PMS5003
from vcgencmd import Vcgencmd

# import ST7735
import time
import pyaudio
import audioop
import math


class sensors:
    def __init__(self) -> None:
        pass

    def poll(self) -> None:
        pass

    class BME280:
        def __init__(self) -> None:
            self.BME280 = BME280()

        def poll(self) -> dict[str, float]:
            temperature: float = round(
                self.BME280.get_temperature() - self.calibrate(), 2
            )
            pressure: float = round(self.BME280.get_pressure(), 2)
            humidity: float = round(self.BME280.get_humidity(), 2)
            return {
                "temperature": temperature,
                "pressure": pressure,
                "humidity": humidity,
            }

        def calibrate(self, factor=0.10) -> float:
            vcGenCMD = Vcgencmd()
            cpuTemp = vcGenCMD.measure_temp()
            return round(cpuTemp * factor, 2)

    class LTR559:
        def __init__(self) -> None:
            self.LTR559 = LTR559()

        def poll(self) -> dict[str, int]:
            lux: float = round(self.LTR559.get_lux(), 2)
            proximity: float = round(self.LTR559.get_proximity(), 2)
            return {"lux": lux, "proximity": proximity}

    class MICS6814:
        def __init__(self) -> None:
            pass

        def poll(self) -> dict[str, float]:
            return gas.read_all()

    class PMS5003:
        def __init__(self) -> None:
            self.PMS5003 = PMS5003()

        def poll(self) -> dict[str, float]:
            pmReadings = self.PMS5003.read()
            pmOne = pmReadings.pm_ug_per_m3(1.0, atmospheric_environment=True)
            pmTwoDotFive = pmReadings.pm_ug_per_m3(2.5, atmospheric_environment=True)
            pmTen = pmReadings.pm_ug_per_m3(None, atmospheric_environment=True)
            return {"pmOne": pmOne, "pmTwoDotFive": pmTwoDotFive, "pmTen": pmTen}

    class Microphone:
        # Some constants for setting the PyAudio and the
        # Aubio.
        BUFFER_SIZE = 2048
        CHANNELS = 1
        FORMAT = pyaudio.paFloat32
        METHOD = "default"
        SAMPLE_RATE = 44100
        HOP_SIZE = BUFFER_SIZE // 2
        PERIOD_SIZE_IN_FRAME = HOP_SIZE

        def __init__(self) -> None:
            pass

        def poll(self) -> dict[str, float]:
            pA = pyaudio.PyAudio()
            mic = pA.open(
                format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.SAMPLE_RATE,
                input=True,
                input_device_index=0,
                frames_per_buffer=self.PERIOD_SIZE_IN_FRAME,
            )
            data = mic.read(self.PERIOD_SIZE_IN_FRAME)
            rms = audioop.rms(data, 2)
            decibel = 20 * math.log10(rms)
            mic.close()
            return {"decibel": decibel}

        def poll(self) -> None:
            pass
