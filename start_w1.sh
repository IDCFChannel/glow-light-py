#!/bin/bash
sudo sh -c 'echo BB-W1:00A0 > /sys/devices/bone_capemgr.9/slots'
/home/debian/python_apps/glow-light-py/w1_publish.py

