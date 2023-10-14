import unittest
from ejercicio1 import is_palindrome

class UnitTestExerciseOne(unittest.TestCase):
    
    # This function gives 3 examples of dirent types of variables to check 
    def test_with_numbers(self):
        self.assertFalse(is_palindrome(5768))
        self.assertFalse(is_palindrome("85.6"))
        self.assertFalse(is_palindrome([6,7,8,'Hola']))
        self.assertFalse(is_palindrome({"word": 2}))


unittest.main()


