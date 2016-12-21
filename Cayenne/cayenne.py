import paho.mqtt.client as paho

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload)) 
    payload = str(msg.payload).split(",")
    client.publish('v1/username/things/clientID/data/channel', payload[1], qos=0)

#Connect to Cayenne
client = paho.Client(client_id='clientID')
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_message = on_message
client.username_pw_set('Username', 'Password')
client.connect(host='mqtt.mydevices.com', port=1883, keepalive=60)
client.subscribe(('v1/username/things/clientID/cmd/channel', 0))

client.loop_forever()