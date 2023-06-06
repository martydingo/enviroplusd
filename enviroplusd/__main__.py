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
    f"{homeassistant_mqtt_autodiscover_prefix}/sensor/climate-{node_id}"
)

enviroplusd_mqtt_topic_prefix = f"climate/{node_id}"

haClimateDiscoveryTopics = {
    "temperature": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/temperature/config",
        "payload": {
            "name": "temperature",
            "object_id": "temperature",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/temperature/state",
        },
    },
    "pressure": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/pressure/config",
        "payload": {
            "name": "pressure",
            "object_id": "pressure",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/pressure/state",
        },
    },
    "humidity": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/humidity/config",
        "payload": {
            "name": "humidity",
            "object_id": "humidity",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/humidity/state",
        },
    },
    "lux": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/lux/config",
        "payload": {
            "name": "lux",
            "object_id": "lux",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/lux/state",
        },
    },
    "proximity": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/proximity/config",
        "payload": {
            "name": "proximity",
            "object_id": "proximity",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/proximity/state",
        },
    },
    "gas/reducing": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/gas/reducing/config",
        "payload": {
            "name": "reducing",
            "object_id": "reducing",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/gas/reducing/state",
        },
    },
    "gas/oxidising": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/gas/oxidising/config",
        "payload": {
            "name": "oxidising",
            "object_id": "oxidising",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/gas/oxidising/state",
        },
    },
    "gas/nh3": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/gas/nh3/config",
        "payload": {
            "name": "nh3",
            "object_id": "nh3",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/gas/nh3/state",
        },
    },
    "pm/One": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/pm/One/config",
        "payload": {
            "name": "One",
            "object_id": "One",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/pm/One/state",
        },
    },
    "pm/TwoDotFive": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/pm/TwoDotFive/config",
        "payload": {
            "name": "TwoDotFive",
            "object_id": "TwoDotFive",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/pm/TwoDotFive/state",
        },
    },
    "pm/Ten": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/pm/Ten/config",
        "payload": {
            "name": "Ten",
            "object_id": "Ten",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/pm/Ten/state",
        },
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
