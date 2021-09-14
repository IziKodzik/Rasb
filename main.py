import random
from datetime import datetime
from threading import Thread
from gpiozero import LED, Pin, Button, DigitalInputDevice
from time import sleep
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
        sleep(1)
        led.off()
        sleep(0.25)


def raspberry_program():
    thread = Thread(target=blink_led).start()

    button = Button(2)
    button.hold_time = 1
    last_button_state = button.is_active
    first = -1
    while True:
        if button.is_active and first < 0:
            first = time.time()*1000
        else:
            first = -1
        if time.time()*1000 - first > 1:
            print("co jest kurwa?")
            first = -1



if __name__ == '__main__':
    note_boot()
    raspberry_program()
