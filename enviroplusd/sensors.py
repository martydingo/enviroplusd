from bme280 import BME280
from ltr559 import LTR559
from pms5003 import PMS5003

# from vcgencmd import Vcgencmd
# import ST7735
import time
import enviroplus.gas


class sensors:
    def __init__(self) -> None:
        pass

    def poll(self) -> None:
        pass

    class BME280:
        def __init__(self) -> None:
            self.BME280 = BME280()

        def poll(self) -> dict[str, float]:
            temperature: float = (
                round(self.BME280.get_temperature(), 2) - self.calibrate()
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
        def __init__(self) -> None:
            pass

        def poll(self) -> None:
            pass
