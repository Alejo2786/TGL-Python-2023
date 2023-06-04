#Write a Python program that prints the first 10 Fibonacci numbers using a loop

def fibonacci():      # The series starts from 0 and 1
    a = 0 
    b = 1

    for i in range(10):       # "Iterate 10 times to generate the 10 numbers."

        print(a)         # "Print the updated value of 'a' as the next number in the series.(0, 1, 1, 2, 3, 5, 8, 13, 21, 34)" 

        c = a + b        # "The value of the sum of 'a' and 'b' is stored in a temporary variable."
        a = b            # "The values of 'a' and 'b' are updated to follow the pattern of the series."
        b = c

def main():
    fibonacci()


if __name__ == '__main__':
    main()