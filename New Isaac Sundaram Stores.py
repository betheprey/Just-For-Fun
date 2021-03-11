a=1
while a==1:
    print("\n           WELCOME TO NEW ISAAC SUNDARAM STORES")
    print("     ")
    print("     ")
    print("     OPTIONS")
    print("     ")
    print("1. Scrap Metal Calculation")
    print("2. Live Metal Calculation")
    print("3. Salary Calculation")
    print("4. Workers List")
    print("5. About")
    print("0. Exit")
    b=int(input("Enter Value : "))
    if b==0:
        break
    while b==1:
        import os
        os.system('cls')
        print("\n")
        print("         Welcome To Scrap Rate Calculation")
        print("\n")
        print("1. Iron")
        print("2. Copper")
        print("3. Aluminium")
        print("4. Brass")
        print("5. Plastic")
        print("6. Steel")
        print("7. Tin")
        print("8. Lead")
        print("0. Back")
        c=int(input("Enter Value : "))
        if c==0:
            import os
            os.system('cls')
            break
        elif c==1:
            import os
            os.system('cls')
            weight=int(input("Weight of Iron (Kg) : "))
            rate=20
            total=weight*rate
            print("       ")
            print("Total =",total)
            input("Press Enter To Continue ...")
        elif c==2:
            import os
            os.system('cls')
            print("\n   Select Copper Type ")
            print("     ")
            print("1. Dynamic Copper")
            print("2. Industrial Copper")
            print("3. New Copper")
            print("4. Old Copper")
            input("Press Enter To Continue ...")
        elif c==3:
            import os
            os.system('cls')
            weight=int(input("Weight of Aluminium (Kg) : "))
            rate=80
            total=weight*rate
            print("       ")
            print("Total =",total)
            input("Press Enter To Continue ...")
        elif c==4:
            import os
            os.system('cls')
            weight=int(input("Weight of Brass (Kg) : "))
            rate=120
            total=weight*rate
            print("       ")
            print("Total =",total)
            input("Press Enter To Continue ...")
        elif c==5:
            import os
            os.system('cls')
            print("\n   Select Plastic Type")
            print("     ")
            print("1. Hard Plastic")
            print("2. New Plastic")
            print("3. Old Plastic")
            input("Press Enter to Continue ...")
        elif c==6:
            import os
            os.system('cls')
            weight=int(input("Weight of Steel (Kg) : "))
            rate=30
            total=weight*rate
            print("       ")
            print("Total =",total)
            print("       ")
            input("Press Enter To Continue ...")
        elif c==7:
            import os
            os.system('cls')
            weight=int(input("Weight of Tin (Kg) : "))
            rate=10
            total=weight*rate
            print("       ")
            print("Total =",total)
            print("       ")
            input("Press Enter To Continue ...")
        elif c==8:
            import os
            os.system('cls')
            weight = int(input("Weight of Lead (Kg) : "))
            rate = 100
            total = weight * rate
            print("       ")
            print("Total =", total)
            print("       ")
            input("Press Enter To Continue ...")
        else:
            import os
            os.system('cls')
            print("INVALID RESPONSE")






