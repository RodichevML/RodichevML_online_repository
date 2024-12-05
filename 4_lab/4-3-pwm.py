import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)

p = GPIO.PWM(27, 1)
p.start(50)
input('Press return to stop: ')

try:
    while (True):
        duty_cycle = int(input("Введите коэффициент заполнения: "))
        p.ChangeDutyCycle(duty_cycle)
finally:
    p.stop()
    GPIO.cleanup()