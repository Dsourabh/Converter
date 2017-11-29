#!/usr/bin/env python3
print("converter Fahrenheit and celcius")
while 'true':
    print("\n\n\t 1: Fahrenheit > Celcius""\n\t 2: Celcius > Fahrenheit""\n\t 3: Exit")
    print("Enter your Option")
    option = int(input(""))
    if option == 1 or option == 2:
        while 'true':
            if option == 1: 
                print("Fahrenheit to Celcius")
                fahrenheit = float(input(""))
                celcius = (fahrenheit-32)/1.8
                print("celcius %f" % (celcius))
                break
            elif option == 2:
                print("Celcius to Fahrenheit ")
                celcius = float(input(""))
                fahrenheit = (celcius * 1.8) + 32
                print("Fahrenheit %f" % (fahrenheit))
                break
    elif option == 3:
        quit()
    else:
        continue






