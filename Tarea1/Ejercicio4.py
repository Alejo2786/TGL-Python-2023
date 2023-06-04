# • Exercise 2Create a Python program that checks if a given number is prime or not. The user should input a number, and the program should print whether it is prime or not.


def prime():
    while True:

        num = int(input("Please Enter a positive integer number to check if it is prime or not: ")) 

        if num <= 0:

            print("Please Enter a positive integer number")    # Display error message if non-positive integer is entered

        else: break                                            # Break out of the loop if a valid positive integer is entered

    if num == 1:

        print(f"the number {num} is not prime")                # 1 is not considered a prime number         

    else:
        div = 0

        for i in range(2, num):             # the loop iterates through the range from 2 to num (exclusive) and checks if the number is divisible by any value within that range.

            if num % i == 0:

                div += 1

                break                                          # If a divisor is found, set div to 1 and exit the loop using break

        if div > 0:

            print(f"the number {num} is not prime")             # If div > 0, a divisor was found, so the number is not prime

        else:

            print(f"the number {num} is prime")                   # If div = 0, no divisor was found, so the number is prime

            
        


def main():
    while True:
      
      prime()

      restart = input("Do you want to do it again? (y/n): ")   # Prompt the user to enter 'y' or 'n' to restart or exit

      if restart.lower() != "y":

        break                                      # If the user enters anything other than 'y', break out of the loop and exit the program

if __name__ == '__main__':
    main()
