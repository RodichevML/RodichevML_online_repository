import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

Volts = []

try:
    flag = 0
    t_begin = time.time()
    GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
    while True:
        N = 0
        for i in range(7, -1, -1):
            N += 2**i
            dec_i = [int(bit) for bit in bin(N)[2:].zfill(8)]
            GPIO.output(dac, dec_i)
            time.sleep(0.006)
            compValue = GPIO.input(comp)
            if compValue == 1:
                N -= 2**i
        digital_value = N
        Voltage = digital_value / 256 * 3.3
        if Voltage > 2.6 and flag == 0: 
            flag = 1
            GPIO.output(troyka, GPIO.LOW)
        Volts.append(Voltage)
        print(digital_value, Voltage)
        if flag and Voltage < 2.28:
            break
    t_end = time.time()   
    time_of_experiment = t_end - t_begin
    avg_descritisation_frequency = len(Volts)/time_of_experiment
    with open('/home/b03-404/Desktop/Repositories/get/RodichevML_main_repository/settings.txt', 'w') as f_of_desc:
        f_of_desc.write(f'{avg_descritisation_frequency}')
    with open('/home/b03-404/Desktop/Repositories/get/RodichevML_main_repository/data.txt', 'w') as f_of_data:
        for i in range(len(Volts)):
            f_of_data.write(str(Volts[i]) + '\n')
    number_of_experiment = [i for i in range(1, len(Volts) + 1)]
    plt.plot(number_of_experiment, Volts)
    print(f'Общая продолжительность эксперимента: {round(time_of_experiment,2)}')
    print(f'Колво измерений {len(Volts)}')
    print(f'Период {round(time_of_experiment/len(Volts), 2)}')
    print(f'Частота {round(len(Volts)/time_of_experiment, 2)}')
    print(f'Шаг квантования: {3.3 / 256}')
    plt.show()

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()