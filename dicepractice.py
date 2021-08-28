import random

print("Hello People, This is Dice Roll Game")

x = "y"

while x == "y":

    
    label = random.randint(0,6)

    
    if label == 1 :
        print("[---------]")
        print("[|       |]")
        print("[    0    ]")
        print("[|       |]")
        print("[---------]")
    if label == 2 :
        print("[---------]")
        print("[|       |]")
        print("[  0   0  ]")
        print("[|       |]")
        print("[---------]")
    if label == 3 :
        print("[---------]")
        print("[|0      |]")
        print("[    0    ]")
        print("[|      0|]")
        print("[---------]")
    if label == 4 :
        print("[---------]")
        print("[| 0   0 |]")
        print("[         ]")
        print("[| 0   0 |]")
        print("[---------]")
    if label == 5 :
        print("[---------]")
        print("[| 0   0 |]")
        print("[    0    ]")
        print("[| 0   0 |]")
        print("[---------]")
    if label == 6 :
        print("[---------]")
        print("[| 0   0 |]")
        print("[  0   0  ]")
        print("[| 0   0 |]")
        print("[---------]")
    x = input("Press Y if you wanna roll again: ")