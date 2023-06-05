#Write a Python function called is_palindrome that checks if a given word is a palindrome. The function should have proper error handling and be tested with unittest.

def is_palindrome(word):

    if not word.isalpha():                                                       # Check if the word contains only letters
        raise ValueError("Please you must only imput letters, try again")
    
    rev_given_word = word[::-1]                                                  # Reverse the word

    if word == rev_given_word:                                                   # Compare the word with its reversed version
        return True
       
    else:
        return False


def main():
    while True:

        given_word = input("Please enter a word to check if it is a palindrome: ").lower()     # Prompt the user to enter a word and convert it to lowercase

        if is_palindrome(given_word):        
         print(f"The word '{given_word}' is a palindrome")

        else:
           print(f"The word '{given_word}' is not a palindrome")

        restart = input("Do you want to enter another word? (y/n): ")   # Prompt the user to enter 'y' or 'n' to restart or exit

        if restart.lower() != "y":                           # Exit the loop if the user does not want to enter another word

          break                             



if __name__ == '__main__':
    main()