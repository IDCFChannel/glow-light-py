#!/usr/bin/python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
from time import sleep
import json
import sys
from config import conf

w1="/sys/bus/w1/devices/28-0414708c9eff/w1_slave"

def sensing():
    raw = open(w1, "r").read()
    celsius = float(raw.split("t=")[-1])/1000
    retval = dict(temperature="{:.2f}".format(celsius))
    return retval

def on_connect(client, userdata, rc):
    print("Connected with result code {}".format(rc))

def on_publish(client, userdata, mid):
    print("publish: {}".format(mid))

def main():
    client = mqtt.Client(client_id='',
	                 clean_session=True, protocol=mqtt.MQTTv311)

    client.username_pw_set(conf["TRIGGER_UUID"], conf["TRIGGER_TOKEN"])

    client.on_connect = on_connect
    client.on_publish = on_publish

    client.connect(conf["IDCF_CHANNEL_URL"], 1883, 60)

    while True:
        retval = sensing()
        if retval:
             message = json.dumps({"devices":
	                       conf["FREEBOARD_UUID"],
                              "payload": retval})
             print(message)
             client.publish("message",message)
        sleep(5)

if __name__ == '__main__':
    main()

