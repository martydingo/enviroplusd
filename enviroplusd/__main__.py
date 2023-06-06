from .sensors import sensors
from .mqtt import mqtt
import yaml

climateConfig: dict[str, str] = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)[
    "climate"
]

bme280_data = sensors.BME280().poll()
ltr559_data = sensors.LTR559().poll()
mics6814_data = sensors.MICS6814().poll()

climate = {
    "temperature": bme280_data["temperature"],
    "pressure": bme280_data["pressure"],
    "humidity": bme280_data["humidity"],
    "lux": ltr559_data["lux"],
    "proximity": ltr559_data["proximity"],
    "gas": {
        "reducing": mics6814_data["reducing"],
        "oxidising": mics6814_data["oxidising"],
        "nh3": mics6814_data["nh3"],
    },
}


if climateConfig["sensors"]["pms5003"] == True:
    pms5003_data = sensors.PMS5003().poll()
    climate["pmOne"] = pms5003_data["pmOne"]
    climate["pmTwoDotFive"] = pms5003_data["pmTwoDotFive"]
    climate["pmTen"] = pms5003_data["pmTen"]

print(climate)