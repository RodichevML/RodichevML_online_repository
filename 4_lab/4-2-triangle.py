import RPi.GPIO as GPIO
import time

def decimal_to_binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    T = int(input('Введите период ')) 
    while(True): 
        for i in range(256):
            GPIO.output(dac, decimal_to_binary(i))
            time.sleep(T/512)
        for i in range(255, -1, -1):
            GPIO.output(dac, decimal_to_binary(i))
            time.sleep(T/512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()