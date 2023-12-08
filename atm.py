balance  = 110000
pin = 1123

while True:
    print("\n")
    print("welcome to sbi bank" .center(90))
    print("*"*100)
    print(" menu options".center(90))
    print("1. check balance ".center(90))
    print(" 2. withdrawal ".center(90))
    print(" 3. Deposite  ".center(90))
    print("4. change pin  ".center(90))
    print("5. exit ".center(90))
    print("*"*100)

    n = input("\n enter your choice : ")

    if n== "1":
        k = int(input(" enter pin" ))
        if pin ==k :
            print( "\n your balance is rs.", balance)
        else:
            print(" \n invalid pin ")
    elif n == "2":
        k = int(input("enter the pin :"))
        if pin == k:
            withdraw= int(input(" withdrawal amount : " ))
            if balance >= withdraw:
                balance -= withdraw
                print("\n withdraw success ful")
                print("\n balance amount is " , balance)
            else:
                balance <= withdraw
                print("\n the amount is not valid ")
        else:
            print("\n the pin is invalid")
    elif n == "3":
        k = int(input("enter thepin :" ))
        if pin == k:
            
            deposite = int(input(" enter the deposite amt:" ))
            if deposite <=0:
                print("\n this is invalid :")
            else:
                print("\n the amt succesfully deposited")
                balance += deposite
                print("\n  the total amt :" , balance )
        else:
            print("\n the pin is in valid ")
    elif n == "4":
        k = int(input("enter the pin : " ))
        if k == pin:
            v= int(input(" enter the new pin :" ))
            if v == pin:
                print("\n the pin is altreday used ? ")
            else:
                pin = v
                print(" \n the pin generated succesfully! ")
                print("\n the new pin is : " , pin)
        else:
            print(" \n the pin is same it camnt be used ganerate new pin ^ ")
    elif n =="5":
        print(" exited ")
        break

print(" \n thankyou")
