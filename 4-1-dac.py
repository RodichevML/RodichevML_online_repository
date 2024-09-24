import RPi.GPIO as GPIO

def decimal_to_binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while(True): 
        number = input('Введите число от 0 до 255 ')
        if number == 'q':
            break
        else: 
            number = int(number)
        GPIO.output(dac, decimal_to_binary(number))
        #расчёт и вывод
        print(f"{(3.3 * (number - 1) / 256):.2f}")
except ValueError:
    print('Неверный ввод')
except RuntimeError:
    print('Это число больше 255')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
