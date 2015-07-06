#!/usr/bin/env python
import time

w1 = "/sys/bus/w1/devices/28-0414708c9eff/w1_slave"

while True:
    raw = open(w1, "r").read()
    celsius = float(raw.split("t=")[-1])/1000 
    print("Temperature is {0:.2f} degrees".format(celsius))
    time.sleep(5)

