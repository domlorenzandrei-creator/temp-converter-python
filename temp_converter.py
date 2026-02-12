def title():
    print('Temperature Converter')




while True:
        title()
        choice = input("Enter your choice (C to F or F to C) (C/F): ")
        if choice == "C" or choice == "c":
                celsius = float(input("Enter Celsius: "))
                fah = (celsius * 9 / 5) + 32
                print(f'Temperature: {celsius:.2f} celsius is equal to {fah:.2f} fahrenheit!')
        elif choice == "F" or choice =="f":
            fahrenheit = float(input("Enter Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print(f'Temperature: {fahrenheit:.2f} fahrenheit is equal to {celsius:.2f} celsius!')
        else:
             print('Please enter a valid choice')
             print("Goodbye")
             break