import RPi.GPIO as GPIO
import time
def decimal_to_binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    N = 0
    
    for i in range(7, -1, -1):
        N += 2**i
        dec_i = decimal_to_binary(N)
        GPIO.output(dac, dec_i)
        time.sleep(0.01)
        compValue = GPIO.input(comp)
        if compValue == 1:
            N -= 2**i
    return N

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
leds = [2,3,4,17,27,22,10,9]

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

try:
    while True:
        
        digital_value = adc()
        for_leds = decimal_to_binary(digital_value)
        flag = 0
        for i in range(len(for_leds)):
            if for_leds[i] == 1:
                flag = 1
            GPIO.output(leds[i], flag)
        Voltage = digital_value / 256 * 3.3
        print(digital_value, Voltage)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()