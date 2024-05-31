from random import randint

suit = ["gunting", "batu", "kertas"]
komputer = suit[randint(0, 2)]
pemain = False


while pemain==False:
    pemain = input("gunting, batu, kertas?")

    if pemain==komputer:
        print("permaianan seri")
    
    elif pemain=="gunting":
        if komputer=="kertas":
            print("pemain menang", pemain, "memotong", komputer)
        else:
            print("komputer menang", komputer, "menghancurkan", pemain)

    elif pemain=="batu":
        if komputer=="gunting":
            print("pemain menang", pemain, "menghancurkan", komputer)
        else:
            print("komputer menang", komputer, "menutupi", pemain)

    elif pemain=="kertas":
        if komputer=="batu":
            print("pemain menang", pemain, "menutupi", komputer)
        else:
            print("komputer menang", komputer, "mengunting", pemain)
    
    else:
        print("eits itu engak masuk buku ya, coba yang lain!!!")
    
    pemain = False
    komputer = suit[(randint(0, 2))]
    