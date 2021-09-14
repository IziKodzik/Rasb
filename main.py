from datetime import datetime

if __name__ == '__main__':
    stre = f"boot{datetime.now()}"
    print(stre)
    stre = stre.replace('-', '_')
    stre = stre.replace('.', '_')
    stre = stre.replace(':', '_')
    stre = stre.replace(" ", "")
    print(stre)
    f = open(stre, "x")
    f.close()
