from paho.mqtt import client as pahoMqtt
import yaml, time


class mqtt:
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

    def __init__(self) -> None:
        config: dict[str, str] = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)

        self.mqttClient = pahoMqtt.Client()
        self.mqttClient.on_connect = self._on_connect_
        self.mqttClient.username_pw_set(config["mqtt"]["username"], config["mqtt"]["password"])
        
        if config["mqtt"]["tls"]:
            self.mqttClient.tls_set()

        self.mqttClient.connect(config["mqtt"]["host"], config["mqtt"]["port"])
        self.mqttClient.loop_start()
        
        time.sleep(5)
        
        print(self.mqttClient.is_connected())

    def publish(self, topic, value):
        self.client.publish(topic, str(value))
