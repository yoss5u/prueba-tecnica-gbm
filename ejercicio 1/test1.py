import unittest
from ejercicio1 import is_palindrome

class UnitTestExerciseOne(unittest.TestCase):
    
    # This function gives 3 examples of a palindrome
    def test_palindrome(self):
        self.assertTrue(is_palindrome('Reconocer'))
        self.assertTrue(is_palindrome('SalAs'))
        self.assertTrue(is_palindrome('Anita lava la tiNa'))


unittest.main()