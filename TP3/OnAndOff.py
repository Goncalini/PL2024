import re
import sys

def onoff ():
    listaux = []
    sum = 0
    switch = False
    for line in sys.stdin:
        capture = re.findall(r'(on|off|=|\d)', line, re.IGNORECASE)
        listaux.append(capture)
    lista = [item for sublist in listaux for item in sublist]
    for i in lista:
        if i.lower() == "on":
            switch = True
        elif i.lower() == "off":
            switch = False
        elif i.isdigit() and switch:
            sum += int(i)
        elif i.lower() == "=":
            print("Somatório atual = ",sum)
            
def main():
    onoff()

if __name__ == "__main__":
    main()
