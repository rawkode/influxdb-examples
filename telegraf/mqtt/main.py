import paho.mqtt.client as mqtt
import json
import pprint
import time

dict_msg = {
    "contact": True,
    "something": 1.5,
    "temperature": 20.5,
    "my_field": "awesome",
}
msg = json.dumps(dict_msg)

pprint.pprint(msg)

MQTT_HOST = "mqtt"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45

count = 0


def on_publish(client, userdata, mid):
    print("Message Published to MQTT ...")


mqttc = mqtt.Client()
mqttc.on_publish = on_publish
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

mqttc.publish("sensors", msg)

mqttc.disconnect()
time.sleep(2)
