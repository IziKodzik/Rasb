import random
from datetime import datetime
from threading import Thread
from gpiozero import LED, Pin, Button, DigitalInputDevice
import RPi.GPIO as GP
from time import sleep
import os
import time


def note_boot():
    inited = datetime.now()
    boot_file_name = f"/home/pi/Desktop/boots/boots.txt"
    f = open(boot_file_name, "a")
    f.write(f"{inited}\n")
    f.close()


def blink_led():
    led = LED(14)
    while True:
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)


def run_sub_program():
    os.system('sudo python3 /home/pi/Desktop/work/raspb-controller/main.py')


def raspberry_program():
    Thread(target=blink_led).start()

    button = Button(2)
    while True:
        print('ready')
        button.wait_for_active()
        print('compiling')
        os.system('cd /home/pi/Desktop/work/raspb-controller ; sudo git pull')
        sub = Thread(target=run_sub_program).start()
        info = os.system('ps -aux | grep /home/pi/Desktop/work/raspb-controller/main.py')
        print(info)
        button.wait_for_inactive()


if __name__ == '__main__':
    note_boot()
    raspberry_program()
