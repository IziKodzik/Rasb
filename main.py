from datetime import datetime
import gpiozero as gpio
from gpiozero import LED
from time import sleep


def note_boot():
    inited = datetime.now()
    boot_file_name = f"/home/pi/Desktop/boots/boots.txt"
    f = open(boot_file_name, "a")
    f.write(f"{inited}\n")
    f.close()


def raspberry_program():
    led = LED(14)
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)


if __name__ == '__main__':
    note_boot()
    raspberry_program()

