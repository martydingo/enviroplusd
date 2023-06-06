from .sensors import sensors
from .mqtt import mqtt
import yaml

config: dict[str, str] = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)

bme280_data = sensors.BME280().poll()
ltr559_data = sensors.LTR559().poll()
mics6814_data = sensors.MICS6814().poll()

homeassistant_mqtt_autodiscover_prefix = config["homeassistant"]["autodiscover_prefix"]
node_id = config["mqtt"]["node_id"]

homeassistant_mqtt_topic_prefix = (
    f"{homeassistant_mqtt_autodiscover_prefix}/sensor/{node_id}/"
)

haClimateDiscoveryTopics = {
    "temperature": {
        "payload": {
            "name": "temperature",
            "object_id": "temperature",
            "config_topic": f"{homeassistant_mqtt_topic_prefix}/temperature/config",
        }
    },
    "pressure": {
        "payload": {
            "name": "pressure",
            "object_id": "pressure",
            "config_topic": f"{homeassistant_mqtt_topic_prefix}/pressure/config",
        }
    },
    "humidity": {
        "payload": {
            "name": "humidity",
            "object_id": "humidity",
            "config_topic": f"{homeassistant_mqtt_topic_prefix}/humidity/config",
        }
    },
    "lux": {
        "payload": {
            "name": "lux",
            "object_id": "lux",
            "config_topic": f"{homeassistant_mqtt_topic_prefix}/lux/config",
        }
    },
    "proximity": {
        "payload": {
            "name": "proximity",
            "object_id": "proximity",
            "config_topic": f"{homeassistant_mqtt_topic_prefix}/proximity/config",
        }
    },
    "gas/reducing": {
        "payload": {
            "name": "reducing",
            "object_id": "reducing",
            "config_topic": f"{homeassistant_mqtt_topic_prefix}/gas/reducing/config",
        }
    },
    "gas/oxidising": {
        "payload": {
            "name": "oxidising",
            "object_id": "oxidising",
            "config_topic": f"{homeassistant_mqtt_topic_prefix}/gas/oxidising/config",
        }
    },
    "gas/nh3": {
        "payload": {
            "name": "nh3",
            "object_id": "nh3",
            "config_topic": f"{homeassistant_mqtt_topic_prefix}/gas/nh3/config",
        }
    },
    "pm/One": {
        "payload": {
            "name": "One",
            "object_id": "One",
            "config_topic": f"{homeassistant_mqtt_topic_prefix}/pm/One/config",
        }
    },
    "pm/TwoDotFive": {
        "payload": {
            "name": "TwoDotFive",
            "object_id": "TwoDotFive",
            "config_topic": f"{homeassistant_mqtt_topic_prefix}/pm/TwoDotFive/config",
        }
    },
    "pm/Ten": {
        "payload": {
            "name": "Ten",
            "object_id": "Ten",
            "config_topic": f"{homeassistant_mqtt_topic_prefix}/pm/Ten/config",
        }
    },
}

climate = {
    "temperature": bme280_data["temperature"],
    "pressure": bme280_data["pressure"],
    "humidity": bme280_data["humidity"],
    "lux": ltr559_data["lux"],
    "proximity": ltr559_data["proximity"],
    "gas/reducing": mics6814_data.reducing,
    "gas/oxidising": mics6814_data.oxidising,
    "gas/nh3": mics6814_data.nh3,
}


if config["climate"]["sensors"]["pms5003"] == True:
    pms5003_data = sensors.PMS5003().poll()
    climate["pm/One"] = pms5003_data["pmOne"]
    climate["pm/TwoDotFive"] = pms5003_data["pmTwoDotFive"]
    climate["pm/Ten"] = pms5003_data["pmTen"]

# for key, value in climate.items():
#     mqtt().publish(key, value)

print(haClimateDiscoveryTopics)

print(climate)
