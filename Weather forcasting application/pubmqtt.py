import paho.mqtt as mqtt
import Adafruit_DHT
import time
client=mqtt.Client()
client.connect("ip address of raspberry pi","port number of raspberry pi", 60)
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
while True:
    humidity,temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
    client.publish("temp",temperature)
    client.publish("hum",humidity)
    time.sleep(1)