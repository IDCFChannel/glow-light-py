import time

w1="/sys/bus/w1/devices/28-0414708c9eff/w1_slave"

def fahrenheit2celsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius

while True:
    raw = open(w1, "r").read()
    celsius = float(raw.split("t=")[-1])/1000 
    #celsius = fahrenheit2celsius(fahrenheit) 
    print("Temperature is {0:.2f} degrees".format(celsius))
    #print("Temperature is {0:.2f} degrees".format(fahrenheit))
    time.sleep(1)

