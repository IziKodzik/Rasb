from datetime import datetime

if __name__ == '__main__':
    boot_file_name = f"/home/pi/Desktop/boots/boots.txt"
    f = open(boot_file_name, "a")
    f.write(f"{datetime.now()}")
    f.close()
