#!/usr/bin/python
import sys
import Adafruit_DHT as dht
import subprocess
import time
import os

from datetime import datetime

file_path = os.path.dirname(os.path.realpath(__file__))
output = f'{file_path}/weather.json'

def writeOut(line):
    with open(output, 'a') as fmod:
        fmod.write(',\n')
        fmod.write(line)
    
while True:
    
    humidity, temperature = dht.read_retry(dht.DHT22, 4)
    
    f = (temperature * 9/5) + 32
    
    now = datetime.now()

    dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")
    
    line = '{{"d":"{0}","f":{1:0.1f},"h":{2:0.1f}}}'.format(dt_string, f, humidity)

    print (line)

    writeOut(line)
    
    time.sleep(60.0)