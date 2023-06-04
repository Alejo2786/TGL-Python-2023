# • Exercise 1 Write a Python function called find_maximum that takes a list of numbers as input and returns the maximum number from the list

def find_maximum(numbers: list):
    
    numbers_list = [float(number) for number in numbers.split()]  # Split the input string of numbers into a list of individual numbers and convert them to floats

    if not numbers_list:
        return None 
    
    max_num = max(numbers_list)         # Find the maximum number from the list
    return max_num

   
def main():
    while True:

        numbers = input("Please enter a list of numbers separated by a space: ")    # Prompt the user to enter a list of numbers separated by spaces
        
        maximum = find_maximum(numbers)                                   # Call the find_maximum function with the user's input

        if maximum is None:
            print("The list is empty.")
        
        else:
            print(f"The maximum number in the list is: {maximum}")            # Print the maximum number if it exists
        
        restart = input("Do you want to enter a new list of numbers? (y/n): ")                # Ask the user if they want to perform the operation again
        if restart.lower()!= "y":
         break



if __name__ == '__main__':
    main()