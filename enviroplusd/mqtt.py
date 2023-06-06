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
        mqttConfig: dict[str, str] = self._loadMqttConfig_()
        print(mqttConfig["host"])
        self.mqttClient = pahoMqtt.Client()
        self.mqttClient.on_connect = self._on_connect_
        self.mqttClient.username_pw_set(mqttConfig["username"], mqttConfig["password"])
        if mqttConfig["tls"]:
            self.mqttClient.tls_set()
        self.mqttClient.connect(mqttConfig["host"], mqttConfig["port"])
        time.sleep(5)
        print(self.mqttClient.is_connected())
        self.mqttClient.loop_start()

    def _loadMqttConfig_(self) -> dict[str, str]:
        return yaml.load(open("config.yaml"), Loader=yaml.FullLoader)["mqtt"]

    def publish(self, topic, value):
        prefix = self._loadMqttConfig_()["topic_prefix"]
        topic = f"{prefix}/{topic}"
        self.client.publish(topic, str(value))
