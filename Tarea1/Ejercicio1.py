# Exercise 1: Write a Python program that takes two numbers as input from the user and printstheir sum.

def sum():
  while True:
    a = float(input("Please enter the first number: "))

    b = float(input("Plase enter the second number: "))

    result = a + b

    print(f"the result is: {result}")

    restart = input("Do you want to do it again? (y/n): ")
    if restart.lower()!= "y":
       break

  
def main():
  sum()

if __name__ == '__main__':
    main()

