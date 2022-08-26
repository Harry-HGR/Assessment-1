import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" hi "+str(msg.payload))
    with open ("test.txt", "w") as f:
        f.write(str(msg.payload))
        f.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
