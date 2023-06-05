#Create a Python decorator called timer that measures the time taken to execute a function. Use this decorator on a function that sorts a list of random numbers and
#prints the sorted list.




import time

def timer(funct):                                                   # Decorator function that measures the execution time of the decorated function

    def crono(*args, **kwargs):                                     #  function that measures the execution time

        starting_time = time.time()                                 # Get the starting time

        execution = funct(*args, **kwargs)                          # Call the decorated function

        ending_time = time.time()                                   # Get the ending time

        execution_time = ending_time - starting_time                # Calculate the execution time

        print(f"The function '{funct.__name__}' took {execution_time} seconds to execute")     # Print the execution time with the name of the decorated function

        return execution
    
    return crono




@timer
def sorted_numbers():                                                                             # Function to sort a list of random numbers

    numbers = input("Please enter a list of random numbers separated by a space: ") 

    try:
        numbers_list = [float(number) for number in numbers.split()]                             # Convert input to a list of numbers
    except ValueError as error:
        raise ValueError("Invalid input. Only numeric values are allowed. Try again") from error
    
    if not numbers_list:
         print("The list is empty.")      
            
    else:
        sorted_list = sorted(numbers_list)                                                        # Sort the list of numbers
        print(f"The sorted list is : {sorted_list}")

sorted_numbers()                                                                                  # Call the decorated function to sort the numbers



    



