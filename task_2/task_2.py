# This task involves encrypting/decrypting of messages

import json

decoding = {"a" : "11", "b" : "12", "c" : "13", "d" : "14", "e" : "15", "f" : "16", "g" : "17", "h" : "18", "i" : "19",
 "j" : "20", "k" : "21","l" : "22", "m" : "36", "n" : "37", "o" : "23", "p" : "24", "q" : "25", "r" : "26", "s" : "27", "t" : "28", "u" : "29", 
 "v" : "30", "w" : "31", "x" : "32", "y" : "33", "z" : "34", " " : "35", "." : "38"}

with open("./task_2/key.json", "w") as f:
    json.dump(decoding, f)

choice = input("""Enter your choice:
1. Enter 1 for decryption
2. Enter 2 for encryption
""")
dec = ""

if choice == "1":

    x = input("Input title of message to decode : ")

    n = "./task_2/" + x + ".txt"

    with open(n, "r") as f:
        content = f.read()
        y = len(content)
        for i in range(0,y,2):
            z = content[i] + content[i+1]
            with open("./task_2/key.json") as j:
                keys = json.load(j)
                for k, v in keys.items():
                    if z == v:
                        print(k, end = "")
                        break

elif choice == "2":

    x = input("Enter title of the message : ")
    n = "./task_2/" + x + ".txt"

    with open(n, "w") as f:
        mes = input("Enter message to encrypt : ")
        mes = mes.lower()
        y = len(mes)

        for i in range(y):
            z = mes[i]
            with open("./task_2/key.json") as j:
                keys = json.load(j)
                for k, v in keys.items():
                    if z == k:
                        dec += v
        f.write(dec)
