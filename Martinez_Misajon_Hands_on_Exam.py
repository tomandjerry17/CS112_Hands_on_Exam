def conv():
    print("\nPress 1 (Decimal to Binary)")
    print("Press 2 (Decimal to Octal)")
    print("Press 3 (Decimal to Hexadecimal)")
    print()

    choice = eval(input("Choice: "))
    num = eval(input("Enter Decimal: "))

    if choice == 1:
        print(str(num) + " in binary is " + format(num, "b"))
    elif choice == 2:
        print(str(num) + " in octal is " + format(num, "o"))
    elif choice == 3:
        print(str(num) + " in hexadecimal is " + format(num, "x"))
    else:
        print("\nInvalid Choice Please Try Again")
        print(conv())
    return print(rerun())


def rerun():
    cont = str(input("\n\tWould you like to convert again? Y|N: "))
    if cont == "Y" or cont == "y":
        print(conv())
    elif cont == "N" or cont == "n":
        print("\tthank you for using the converter :)")
    else:
        print("\n\tPag sure")
        print(rerun())
    return " "


print(conv())
