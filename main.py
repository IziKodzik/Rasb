from datetime import datetime
from threading import Thread
from gpiozero import LED, Pin, Button, DigitalInputDevice
from time import sleep


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
    while True:
        if True:
            print(69)
        sleep(1)


if __name__ == '__main__':
    note_boot()
    raspberry_program()
