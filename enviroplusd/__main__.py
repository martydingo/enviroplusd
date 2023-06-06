from .sensors import sensors
from .mqtt import mqtt

bme280_data = sensors.BME280().poll()
climate = {
    "temperature": bme280_data["temperature"],
    "pressure": bme280_data["pressure"],
    "humidity": bme280_data["humidity"],
}
print(climate)
