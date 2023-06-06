from .sensors import sensors
from .mqtt import mqtt
import yaml

__all__ = ["sensors", "mqtt"]

sensorData = {"bme280": {sensors.BME280().poll()}}

climate = {
    "temperature": sensorData["bme280"]["temperature"],
}

print(climate)
