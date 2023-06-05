

import unittest

from Ejercicio9 import is_palindrome

class Test_is_palindrome(unittest.TestCase):

    def test_pailindrome_true(self):                            # Test cases for palindromes that should return True

        self.assertTrue(is_palindrome("ama"))
        self.assertTrue(is_palindrome("kayak"))
        self.assertTrue(is_palindrome("mom"))
        self.assertTrue(is_palindrome("solos"))

    def test_palindrome_false(self):                            # Test cases for non-palindromes that should return False
        
        self.assertFalse(is_palindrome("bootcamp"))
        self.assertFalse(is_palindrome("computer"))
        self.assertFalse(is_palindrome("study"))
        self.assertFalse(is_palindrome("alejandro"))

    def test_palindrome_with_invalid_inputs(self):               # Test cases for invalid inputs that should raise a ValueError

        with self.assertRaises(ValueError):                      # Contains numbers, should raise ValueError
            is_palindrome("452655")
        with self.assertRaises(ValueError):
            is_palindrome(".rotator-")                            # Contains non-alphabetic characters, should raise ValueError
             
             
        

        


