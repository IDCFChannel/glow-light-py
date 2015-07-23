#!/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json
import subprocess
import os

from config import conf

def on_connect(client, userdata, rc):
    print("Connected with result code {}".format(rc))
    client.subscribe(conf["ACTION_3_UUID"])

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def led_on_off(on_off):
    cmd = os.path.abspath(os.path.join(os.path.dirname(__file__), "hub-ctrl"))
    p = subprocess.Popen(["sudo",cmd,
	"-b", "1",
	"-d", conf["DEVICE_NO"],
	"-P", conf["PORT_NO"],
	"-p", on_off], stdout=subprocess.PIPE)
    out, err = p.communicate()
    print(out)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    payload = json.loads(msg.payload)
    on_off_str = payload["data"]
    on_off = "1" if on_off_str == "led-on" else "0"
    led_on_off(on_off)

def main():
    client = mqtt.Client(client_id='',
                         clean_session=True, protocol=mqtt.MQTTv311)

    client.username_pw_set(conf["ACTION_3_UUID"], conf["ACTION_3_TOKEN"])
    
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.connect(conf["IDCF_CHANNEL_URL"], 1883, 60)

    client.loop_forever()

if __name__ == '__main__':
    main()

