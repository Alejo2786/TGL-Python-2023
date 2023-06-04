#Create a Python function called reverse_string that takes a string as input and returns the reversed string.

def reverse_string(sentence):

    if not sentence:            # Check if the sentence is empty
        return None
    
    rev_sen = sentence[::-1]    # Reverse the sentence using slicing
    return rev_sen

    

def main():
    while True:

        sentence = input("Please write the sentence you want to reverse: ")     # Ask the user to enter a sentence

        reversed_sentence = reverse_string(sentence)                             # Call the reverse_string function to obtain the reversed sentence

        if reversed_sentence is None:                                            # Check if the reversed sentence is empty
            print("The String is empty.")
        
        else:
            print(f"The reversed sentence is : '{reversed_sentence}'")           # Print the reversed sentence
        
        restart = input("Do you want to enter a new sentence? (y/n): ")                # Ask the user if they want to perform the operation again
        if restart.lower()!= "y":
         break
    
 

if __name__ == '__main__':
    main()
