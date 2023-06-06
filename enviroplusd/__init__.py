from .sensors import sensors
from .mqtt import mqtt
import yaml

__all__ = ["sensors", "mqtt"]

bme280_data = sensors.BME280().poll()

climate = {
    "temperature": bme280_data["temperature"],
}

print(climate)
