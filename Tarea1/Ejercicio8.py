# Create a Python program that reads a text file and counts the occurrences of each word using a dictionary. The program should print the words and their counts.

import re                     ## Import the 're' module to use regular expressions


def reader(words):
        
        words_counter = {}       # Create an empty dictionary to store word frequencies

        for word  in words:      # Iterate over each word in the list of words         
         
            if word not in words_counter:    # If the word is not already in the dictionary, add it with a frequency of 1
                words_counter[word] = 1

            else:
                words_counter[word] +=1       # If the word is already in the dictionary, increment its frequency by 1

        for word, counter in words_counter.items():                            # Iterate over the word-frequency pairs in the dictionary and print the results
            print(f"The word '{word}' appears {counter} times in the text")

           


def main():
    with open("Ejercicio8.txt", "r") as file:

        string = file.read().lower()                    # Read the contents of the file and convert to lowercase

        words = re.findall(r'\b\w+\b', string)          # Use regular expression to find all words in the text
    
    reader(words)                                       # Pass the words to the reader function for counting and printing


if __name__ == '__main__':
    main()