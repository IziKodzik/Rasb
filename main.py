import random
import re
import signal
import subprocess
import threading
from datetime import datetime
from threading import Thread

import psutil as psutil
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
        led.toggle()
        sleep(1)

# def run_sub_program():
# os.system('sudo python3 /home/pi/Desktop/work/raspb-controller/main.py')


def raspberry_program():
    Thread(target=blink_led).start()
    Thread(target=method_name).start()


def method_name():
    button = Button(2)

    while True:
        print('ready')
        button.wait_for_active()
        print('compiling')
        os.system('cd /home/pi/Desktop/work/raspb-controller ; sudo git pull')
        Thread(target=runProg).start()
        # TODO ask how to avoid +1 coz its dangerous
        button.wait_for_inactive()
        str = os.popen('ps -aux | grep \'python3 /home/pi/Desktop/work/raspb-controller/main.py\'').read()
        str = str.split("\n")
        print(str)
        found = re.findall(r'\d+', str[1])
        print(found)
        print(found[0])
        print(os.popen(f'sudo kill {int(found[1])}'))


if __name__ == '__main__':
    note_boot()
    raspberry_program()


def runProg():
    return os.system('python3 /home/pi/Desktop/work/raspb-controller/main.py')