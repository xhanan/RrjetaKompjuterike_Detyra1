import socket
running = True
while running:
    serverName = ''
    serverPort = 0
    var = input("Shtyp 1 per te vazhduar me IPaddres dhe port default ose shtyp 2 per t'i ndryshuar keto vlera: ")
    if(int(var) != 1):
        serverName = input("Shkruani IP adresen: ")
        port = input("Shkruani Portin: ")
        serverPort = int(port)
    else:
        serverName='localhost'
        serverPort=13000

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        server_address = (serverName,serverPort)
        print("-------------------------UDP SERVER -----------------------")
        print("Per te perzgjedhur sherbimin shkruani njeren nga fjalet kyçe:")
        print("IPADDRESA, PORTI, COUNT, REVERSE, PALINDROME, GAME, GFC, CONVERT, KOHA, LEAPYEAR, FIBONACCI, ENCRYPT")
        print("Nese kerkoni metoden CONVERT opsionet e juaja jane: CmtoFeet,FeettoCm,KmtoMiles,MilesToCm")

        try:
            while True:
                MESSAGE = input("Enter a request: ")
                kerkesa = MESSAGE.lower()
                kerkesa = kerkesa.split()
                try:
                    if kerkesa[0] == "exit":
                        sent = sock.sendto(MESSAGE.encode(), server_address)
                        running = False
                        break
                    elif kerkesa[0] == "ipaddresa":
                        if (len(kerkesa) == 1):
                            sent = sock.sendto(MESSAGE.encode(), server_address)
                        else:
                            print("Ju nuk duhet te jepni parametra te tjer pos IPaddressa")
                            continue
                    elif kerkesa[0] == "porti":
                        if (len(kerkesa) == 1):
                            sent = sock.sendto(MESSAGE.encode(), server_address)
                        else:
                            print("Ju nuk duhet te jepni paramtera te tjer pos Porti")
                    elif kerkesa[0] == "count":
                        if (len(kerkesa) > 1):
                            sent = sock.sendto(MESSAGE.encode(), server_address)
                        else:
                            print("Per te kerkuar kete metod, ju duhet se paku te shkruani edhe nje fjale pas fjales Count!")
                            continue
                    elif kerkesa[0] == "reverse":
                        if (len(kerkesa) < 2):
                            print("Per te kerkuar kete metod, ju duhet se paku te shkruani edhe nje fjale pas fjales Reverse!")
                            continue
                        else:
                            sent = sock.sendto(MESSAGE.encode(), server_address)
                    elif kerkesa[0] == "palindrome":
                        if (len(kerkesa) == 2):
                            sent = sock.sendto(MESSAGE.encode(), server_address)
                        else:
                            print("Per te kerkuar kete metod, ju duhet te shkruani edhe nje fjale pas fjales Palindrome!")
                            continue
                    elif kerkesa[0] == "game":
                        if (len(kerkesa) == 1):
                            sent = sock.sendto(MESSAGE.encode(), server_address)
                        else:
                            print("Per te kerkuar kete metod, ju nuk duhet te shkruani fjale tjera pos Game!")
                            continue
                    elif kerkesa[0] == "gfc":
                        if (len(kerkesa) == 3):
                            if kerkesa[1].isdecimal() and kerkesa[2].isdecimal():
                                sent = sock.sendto(MESSAGE.encode(), server_address)
                            else:
                                print("Parametri i dyte dhe i trete duhet te jete numer dhe jo tekst")
                                continue
                        else:
                            print("Per te kerkuar kete metod, ju duhet se paku te shkruani edhe dy parametra pas fjales GFC!")
                            continue
                    elif kerkesa[0] == "convert":
                        if (len(kerkesa) == 3):
                            if kerkesa[2].isdecimal():
                                sent = sock.sendto(MESSAGE.encode(), server_address)
                            else:
                                print("Parametri i trete duhet te jete numer dhe jo tekst")
                                continue
                        else:
                            print("Per te kerkuar kete metod, ju duhet se paku te shkruani llojin dhe numrin te cilin deshironi qe t'a konvertoni pas fjales Convert!")
                            continue
                    elif kerkesa[0] == "koha":
                        if (len(kerkesa) == 1):
                            sent = sock.sendto(MESSAGE.encode(), server_address)
                        else:
                            print("Ju nuk duhet te shkruani asnje parameter tjeter pas fjales Koha")
                            continue
                    elif kerkesa[0] == "leapyear":
                        if (len(kerkesa) == 2):
                            if (kerkesa[1].isdigit()):
                                sent = sock.sendto(MESSAGE.encode(), server_address)
                            else:
                                print("Ju duhet te shkruani nje numer pas fjales leapyear.")
                                continue
                        else:
                            print("Ju duhet te jepni vetem nje parameter pas fjales Leapyear")
                            continue
                    elif kerkesa[0] == "fibonacci":
                        if (len(kerkesa) == 2):
                            if (kerkesa[1].isdecimal()):
                                sent = sock.sendto(MESSAGE.encode(), server_address)
                            else:
                                print("Ju duhet te shkruani nje numer pas fjales fibonacci.")
                                continue
                        else:
                            print("Ju duhet te jepni vetem nje parameter pas fjales Fibonacci")
                            continue
                    elif kerkesa[0] == "encrypt":
                        if (len(kerkesa) == 3):
                            if(kerkesa[1].isdigit()):
                                sent = sock.sendto(MESSAGE.encode(), server_address)
                            else:
                                print("Ju duhet te shkruani nje numer pas fjales encrypt.")
                                continue
                        else:
                            print("Ju duhet te shkruani numrin e SHIFT dhe fjalet qe deshironi ti enkriptoni pas fjales encrypt")
                            continue
                    else:
                        print("Kerkesa juaj nuk eshte valide")
                        continue
                except Exception as e:
                    print(e)
                    continue


                print('waiting to receive')
                data, server = sock.recvfrom(4096)
                print('received {!r}'.format(data))

        finally:
            print('closing socket')
            sock.close()
    except:
        print("Connection failed")
        continue