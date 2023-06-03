#Exercise 2:Create a Python program that converts a temperature from Fahrenheit to Celsius.The user should enter the temperature in Fahrenheit, and the program should printthe equivalent temperature in Celsius.
#formula: ( °F − 32) × 5/9 =  °C

def celsius():
    while True:

        faren = float(input("Please enter the Fahrenheit degrees to convert them to Celsius: "))

        cel = (faren - 32) * 5/9

        print(f"{faren} degrees Fahrenheit are equivalent to {cel} degrees Celsius ")

        restart = input("Do you want to convert another Farenheit temperature  to Celsius? (y/n): ")
        if restart.lower()!= "y":
         break


def main():
    celsius()


if __name__ == '__main__':
    main()