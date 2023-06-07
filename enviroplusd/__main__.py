from .sensors import sensors
from paho.mqtt import client as pahoMqtt
import yaml, time


def _on_connect_(client, userdata, flags, rc):
    errors = {
        1: "incorrect MQTT protocol version",
        2: "invalid MQTT client identifier",
        3: "server unavailable",
        4: "bad username or password",
        5: "connection refused",
    }

    if rc > 0:
        connection_error = errors.get(rc, "unknown error")
        print("Connection error with result code " + connection_error)
    else:
        print("Connected to MQTT broker")    


config: dict[str, str] = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)

mqttClient = pahoMqtt.Client()
mqttClient.on_connect = _on_connect_
mqttClient.username_pw_set(config["mqtt"]["username"], config["mqtt"]["password"])

if config["mqtt"]["tls"]:
    mqttClient.tls_set()

mqttClient.connect(config["mqtt"]["host"], config["mqtt"]["port"])
mqttClient.loop_start()



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
            "name": f"{node_id.capitalize()} Temperature",
            "unique_id": f"{node_id}_temperature",
            "unit_of_measurement": "°C",
            "object_id": f"{node_id}_temperature",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/temperature",
            "device": {
                "manufacturer": "Pimironi",
                "model": "Enviro+",
                "name": "Office Climate Sensor",
                "identifiers": [
                    "climate"
                ]
            }
        },
    },
    "pressure": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/pressure/config",
        "payload": {
            "name": f"{node_id.capitalize()} Pressure",
            "unique_id": f"{node_id}_pressure",
            "unit_of_measurement": "hPa",
            "object_id": f"{node_id}_pressure",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/pressure",
            "device": {
                "manufacturer": "Pimironi",
                "model": "Enviro+",
                "name": "Office Climate Sensor",
                "identifiers": [
                    "climate"
                ]
            }
        },
    },
    "humidity": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/humidity/config",
        "payload": {
            "name": f"{node_id.capitalize()} Humidity",
            "unique_id": f"{node_id}_humidity",
            "object_id": f"{node_id}_humidity",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/humidity",
            "unit_of_measurement": "%",
            "device": {
                "manufacturer": "Pimironi",
                "model": "Enviro+",
                "name": "Office Climate Sensor",
                "identifiers": [
                    "climate"
                ]
            }
        },
    },
    "lux": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/lux/config",
        "payload": {
            "name": f"{node_id.capitalize()} Lux",
            "unique_id": f"{node_id}_lux",
            "object_id": f"{node_id}_lux",
            "unit_of_measurement": "lux",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/lux",
            "device": {
                "manufacturer": "Pimironi",
                "model": "Enviro+",
                "name": "Office Climate Sensor",
                "identifiers": [
                    "climate"
                ]
            }
        },
    },
    "proximity": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/proximity/config",
        "payload": {
            "name": f"{node_id.capitalize()} Proximity",
            "unique_id": f"{node_id}_proximity",
            "object_id": f"{node_id}_proximity",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/proximity",
            "device": {
                "manufacturer": "Pimironi",
                "model": "Enviro+",
                "name": "Office Climate Sensor",
                "identifiers": [
                    "climate"
                ]
            }
        },
    },
    "gas/reducing": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/reducing-gas/config",
        "payload": {
            "name": f"{node_id.capitalize()} Reducing Gas",
            "unit_of_measurement": "kO",
            "device": {
                "manufacturer": "Pimironi",
                "model": "Enviro+",
                "name": "Office Climate Sensor",
                "identifiers": [
                    "climate"
                ]
            },
            "unique_id": f"{node_id}_gas_reducing",
            "object_id": f"{node_id}_gas_reducing",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/gas/reducing",
        },
    },
    "gas/oxidising": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/oxidising-gas/config",
        "payload": {
            "name": f"{node_id.capitalize()} Oxidising Gas",
            "unique_id": f"{node_id}_gas_oxidising",
            "object_id": f"{node_id}_gas_oxidising",
            "unit_of_measurement": "kO",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/gas/oxidising",
            "device": {
                "manufacturer": "Pimironi",
                "model": "Enviro+",
                "name": "Office Climate Sensor",
                "identifiers": [
                    "climate"
                ]
            }
        },
    },
    "gas/nh3": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/nh3-gas/config",
        "payload": {
            "name": f"{node_id.capitalize()} NH3 Gas",
            "unique_id": f"{node_id}_gas_nh3",
            "unit_of_measurement": "kO",
            "object_id": f"{node_id}_gas_nh3",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/gas/nh3",
            "device": {
                "manufacturer": "Pimironi",
                "model": "Enviro+",
                "name": "Office Climate Sensor",
                "identifiers": [
                    "climate"
                ]
            }
        },
    },
    "pm/One": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/pm-one/config",
        "payload": {
            "name": f"{node_id.capitalize()} PM 1.0",
            "unique_id": f"{node_id}_pm_one",
            "object_id": f"{node_id}_pm_one",
            "unit_of_measurement": "ug/m3",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/pm/One",
            "device": {
                "manufacturer": "Pimironi",
                "model": "Enviro+",
                "name": "Office Climate Sensor",
                "identifiers": [
                    "climate"
                ]
            }
        },
    },
    "pm/TwoDotFive": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/pm-twodotfive/config",
        "payload": {
            "name": f"{node_id.capitalize()} PM 2.5",
            "unique_id": f"{node_id}_pm_two_dot_five",
            "object_id": f"{node_id}_pm_two_dot_five",
            "unit_of_measurement": "ug/m3",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/pm/TwoDotFive",
            "device": {
                "manufacturer": "Pimironi",
                "model": "Enviro+",
                "name": "Office Climate Sensor",
                "identifiers": [
                    "climate"
                ]
            }
        },
    },
    "pm/Ten": {
        "config_topic": f"{homeassistant_mqtt_topic_prefix}/pm-ten/config",
        "payload": {
            "name": f"{node_id.capitalize()} PM 10",
            "unique_id": f"{node_id}_pm_ten",
            "object_id": f"{node_id}_pm_ten",
            "unit_of_measurement": "ug/m3",
            "state_topic": f"{enviroplusd_mqtt_topic_prefix}/pm/Ten",
            "device": {
                "manufacturer": "Pimironi",
                "model": "Enviro+",
                "name": "Office Climate Sensor",
                "identifiers": [
                    "climate"
                ]
            }
            
        },
    },
}
        

try:
    while True:


        bme280_data = sensors.BME280().poll()
        ltr559_data = sensors.LTR559().poll()
        mics6814_data = sensors.MICS6814().poll()
 
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

        for key, value in haClimateDiscoveryTopics.items():
            mqttClient.publish(value["config_topic"], str(value["payload"]).replace("'", '"'), retain=True)

        for key, value in climate.items():
            mqttClient.publish(enviroplusd_mqtt_topic_prefix+"/"+key, value)

        time.sleep(10)
except KeyboardInterrupt:
    mqttClient.disconnect()
    sys.exit(0)