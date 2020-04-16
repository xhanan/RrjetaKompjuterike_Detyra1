#UDP SERVERI
import socket
import datetime
import random


#IPADDRESA
def IPADDRESA():
    return ("IP Adresa e klientit eshte: "+str(address[0]))

#PORTI
def PORTI():
    return ("Klienti eshte duke perdorur portin: "+str(address[1]))

# COUNT
def COUNT(text):
    text = text.lower()
    b = 0
    z = 0
    for x in text:
        if x == 'a' or x == 'e' or x == 'i' or x == 'u' or x == 'o':
            z = z + 1
        elif x >= 'a' and x <= 'z':
            b = b + 1
    return ("Numri i zanoreve: " + str(z) + " numri i bashketingelloreve: " + str(b))

# REVERSE
def REVERSE(text):
    str = ""
    for i in text:
        str = i + str
    return str.strip()

# PALINDROME
def PALINDROME(text):
    str = ""
    for i in text:
        str = i + str

    if text == str:
        return True
    else:
        return False

# GAME
def GAME():
    numbers = set()
    for x in range(5):
        r = random.randint(1, 35)
        numbers.add(r)
    return sorted(numbers)

# GFC
def GFC(num1, num2):
    if (num2 == 0):
        return num1
    else:
        return GFC(num2, num1 % num2)

# CONVERT
def CONVERT(type, num):
    if type == "CMTOFEET":
        converted = num * 0.0328084
        converted = round(converted, 2)
        return converted
    elif type == "FEETTOCM":
        converted = num * 30.48
        converted = round(converted, 2)
        return converted
    elif type == "KMTOMILES":
        converted = num * 0.621371
        converted = round(converted, 2)
        return converted
    elif type == "MILETOKM":
        converted = num * 1.60934
        converted = round(converted, 2)
        return converted

# KOHA
def KOHA():
    return datetime.datetime.now().strftime("Date: %Y-%m-%d \n Time: %H:%M")

# LEAPYEAR
def LEAPYEAR(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 == 0:
        return True
    else:
        return False

# FIBONACCI
def FIBONACCI(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (n - 1) + (n - 2)

#CAESAR ENCRYTPION
def ENCRYPT(s,text):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


udpServer = "localhost"
udpPort = 13000
try:
    UDPsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('starting up on {} port {}'.format(*(udpServer, udpPort)))
    UDPsocket.bind((udpServer,udpPort))
except Exception as e:
    print(e)

try:
    while True:
        print('\nwaiting to receive message')
        data, address = UDPsocket.recvfrom(4096)
        data = data.decode()
        data = data.upper()
        metoda = data.split(" ")
        print("Kerkesa e pranuar nga klienti " + address[0] + ":" + str(address[1]) + " eshte: " + metoda[0])
        if (len(metoda) == 0):
            MESAZHI = "Ju nuk keni derguar ndonje kerkese!"
            continue
        if metoda[0] == "EXIT":
             MESAZHI = "connection lost"
             continue
        elif metoda[0] == "GAME":
            MESAZHI = str(GAME())
        elif metoda[0] == "KOHA":
            MESAZHI = str(KOHA())
        elif metoda[0] == "IPADDRESA":
            MESAZHI = str(IPADDRESA())
        elif metoda[0] == "PORTI":
            MESAZHI = str(PORTI())
        elif metoda[0] == "LEAPYEAR" and len(metoda) == 2:
            MESAZHI = str(LEAPYEAR(int(metoda[1])))
        elif metoda[0] == "FIBONACCI" and len(metoda) == 2:
            MESAZHI = str(FIBONACCI(int(metoda[1])))
        elif metoda[0] == "PALINDROME" and len(metoda) == 2:
            MESAZHI = str(PALINDROME(metoda[1]))
        elif metoda[0] == "GFC" and len(metoda) == 3:
            MESAZHI = str(GFC(int(metoda[1]), int(metoda[2])))
        elif metoda[0] == "CONVERT" and len(metoda) == 3:
            MESAZHI = str(CONVERT(metoda[1], int(metoda[2])))
        elif metoda[0] == "COUNT" and len(metoda) > 1:
            MESAZHI = str(COUNT(data[len(metoda[0]):len(data)]))
        elif metoda[0] == "REVERSE" and len(metoda) > 1:
            MESAZHI = str(REVERSE(data[len(metoda[0]):len(data)]))
        elif metoda[0] == "ENCRYPT" and len(metoda) == 3:
            MESAZHI = str(ENCRYPT(int(metoda[1]), metoda[2]))
        else:
            MESAZHI = "Failed! Kerkesa juaj nuk eshte valide. Ju lutem jepni njeren nga kerkesat valide."

        sent = UDPsocket.sendto(MESAZHI.encode(), address)
        if sent:
            print("Succeded")
except Exception as e:
    print(e)
