import paho.mqtt.client as mqttClient
import time

broker_address = "ip of raspbberry pi"  # Broker address
port = "port of raspberry pi"  # Broker port

client=mqtt.Client()# create new instance
client.connect(broker_address, port=port)  # connect to broker
    while True:
        client.subscribe("temp")
        client.subscribe("hum")
        time.sleep(1)
client.disconnect()