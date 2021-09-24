import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
level = 2**bits
max_voltage = 3.3

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
        inputstr = input("Введите число из отрезка [0;255] или нажмите 'q' для выхода > ")

        if inputstr.isdigit():
            value = int(inputstr)

            if value >= level:
                print("Не понил. > ")
                continue

            signal = bin2dac(value)
            voltage = value / level * max_voltage
            print(" Значение = {:^3} -> {}, вольтаж = {:.2f}".format(value,signal, voltage))
    
        elif inputstr == 'q':
            break
        else:
            print("Введи другое число! ")
            continue

except KeyboardInterrupt:
    print("ooohhhh")

else:
    print('aaahhhh')

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print('NIGHT!!! ') 
            
