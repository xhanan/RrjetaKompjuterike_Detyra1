import socket

running = True
while running:
    serverName = ''
    serverPort = 0
    print("Shtyp 0 per te ndaluar programin.")
    var = input("Shtyp 1 per te vazhduar me IP addresen dhe portin default ose shtyp 2 per t'i ndryshuar keto vlera: ")
    if(int(var) == 2):
        serverName = input("Shkruani IP adresen: ")
        port = input("Shkruani Portin: ")
        serverPort = int(port)
    elif(int(var)==0):
        print("Programi u mbyll")
        running = False
        break
    elif (int(var) == 1):
        serverName='localhost'
        serverPort=13000
    else:
        print("Ju lutem shtypni njerin nga opsionet")
        continue

    tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcpClientA.connect((serverName, serverPort))
        print("-------------------------TCP SERVER -----------------------")
        print("Per te perzgjedhur sherbimin shkruani njeren nga fjalet kyçe:")
        print("IPADDRESA, PORTI, COUNT, REVERSE, PALINDROME, GAME, GFC, CONVERT, KOHA, LEAPYEAR, FIBONACCI, ENCRYPT")
        print("Nese kerkoni metoden CONVERT opsionet e juaja jane: CmtoFeet,FeettoCm,KmtoMiles,MileToCm")
        while running:
            MESSAGE = input("Jeni lidhur me serverin, shkruani kerkesen: ")
            if(len(MESSAGE)>128):
                print("Mesazhi nuk duhet te jete me i madh se 128 karaktere")
                continue
            else:
                kerkesa = MESSAGE.lower()
                kerkesa = kerkesa.split(" ")
                try:
                    if kerkesa[0] == "exit":
                        tcpClientA.send(str.encode(MESSAGE))
                        running = False
                        break
                    elif kerkesa[0] == "ipaddresa":
                        if (len(kerkesa) == 1):
                            tcpClientA.send(str.encode(MESSAGE))
                        else:
                            print("Ju nuk duhet te jepni parametra te tjer pos IPaddressa")
                            continue
                    elif kerkesa[0] == "porti":
                        if (len(kerkesa) == 1):
                            tcpClientA.send(str.encode(MESSAGE))
                        else:
                            print("Ju nuk duhet te jepni paramtera te tjer pos Porti")
                    elif kerkesa[0] == "count":
                        if (len(kerkesa) > 1):
                            tcpClientA.send(str.encode(MESSAGE))
                        else:
                            print("Per te kerkuar kete metod, ju duhet se paku te shkruani edhe nje fjale pas fjales Count!")
                            continue
                    elif kerkesa[0] == "reverse":
                        if (len(kerkesa) < 2):
                            print("Per te kerkuar kete metod, ju duhet se paku te shkruani edhe nje fjale pas fjales Reverse!")
                            continue
                        else:
                            tcpClientA.send(str.encode(MESSAGE))
                    elif kerkesa[0] == "palindrome":
                        if (len(kerkesa) == 2):
                            tcpClientA.send(str.encode(MESSAGE))
                        else:
                            print("Per te kerkuar kete metod, ju duhet te shkruani edhe nje fjale pas fjales Palindrome!")
                            continue
                    elif kerkesa[0] == "game":
                        if (len(kerkesa) == 1):
                            tcpClientA.send(str.encode(MESSAGE))
                        else:
                            print("Per te kerkuar kete metod, ju nuk duhet te shkruani fjale tjera pos Game!")
                            continue
                    elif kerkesa[0] == "gfc":
                        if (len(kerkesa) == 3):
                            if(kerkesa[1].isdecimal() and kerkesa[2].isdecimal()):
                                tcpClientA.send(str.encode(MESSAGE))
                            else:
                                print("Parametrat pas GFC duhet te jene numera dhe jo tekst")
                                continue
                        else:
                            print("Per te kerkuar kete metod, ju duhet se paku te shkruani edhe dy parametra pas fjales GFC!")
                            continue
                    elif kerkesa[0] == "convert":
                        if (len(kerkesa) == 3):
                            if (kerkesa[2].isdecimal()):
                                tcpClientA.send(str.encode(MESSAGE))
                            else:
                                print("Parametrat pas GFC duhet te jene numera dhe jo tekst")
                                continue
                        else:
                            print(
                                "Per te kerkuar kete metod, ju duhet se paku te shkruani llojin dhe numrin te cilin deshironi qe t'a konvertoni pas fjales Convert!")
                            continue
                    elif kerkesa[0] == "koha":
                        if (len(kerkesa) == 1):
                            tcpClientA.send(str.encode(MESSAGE))
                        else:
                            print("Ju nuk duhet te shkruani asnje parameter tjeter pas fjales Koha")
                            continue
                    elif kerkesa[0] == "leapyear":
                        if (len(kerkesa) == 2):
                            if kerkesa[1].isdigit():
                                tcpClientA.send(str.encode(MESSAGE))
                            else:
                                print("Parametri i dyte duhet te jete numer dhe jo tekst")
                                continue
                        else:
                            print("Ju duhet te jepni vetem nje parameter pas fjales Leapyear")
                            continue
                    elif kerkesa[0] == "fibonacci":
                        if (len(kerkesa) == 2):
                            if kerkesa[1].isdigit():
                                tcpClientA.send(str.encode(MESSAGE))
                            else:
                                print("Parametri i dyte duhet te jete numer dhe jo tekst")
                                continue
                        else:
                            print("Ju duhet te jepni vetem nje parameter pas fjales Fibonacci")
                            continue
                    elif kerkesa[0] == "encrypt":
                        if (len(kerkesa) == 3):
                            if kerkesa[1].isdigit():
                                tcpClientA.send(str.encode(MESSAGE))
                            else:
                                print("Parametri i dyte duhet te jete numer dhe jo tekst")
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

                mesazhi = ''
                data = tcpClientA.recv(1024)
                mesazhi += data.decode("utf-8")
                print('Te dhenat e pranuara nga serveri: ', mesazhi)


    except:
        print("Connection failed. Please try again!")
        continue






