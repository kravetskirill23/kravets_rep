import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
max_voltage = 3.3
timeout = float(0.3)

def decimal2binarry(x):
    return [int(i) for i in bin(x)[2:].zfill(bits)]

def bin2dac(value):
    signal = decimal2binarry(value)
    GPIO.output(dac, signal)
    return signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
    while True:
        for j in range(255):
            value = int(j)  
            signal = bin2dac(value)
            time.sleep(0.1)
        for k in range(255,0,-1):
            value = int(k)  
            signal = bin2dac(value)
            time.sleep(0.1)
        
except KeyboardInterrupt:
    print("ooohhhh")

else:
    print('aaahhhh')

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print('NIGHT!!! ') 
            
