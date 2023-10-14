import unittest
from ejercicio1 import is_palindrome

class UnitTestExerciseOne(unittest.TestCase):
    
    # This function gives 3 examples of a non palindrome word of phrase
    def test_fail_palindrome(self):
        self.assertFalse(is_palindrome('Carro'))
        self.assertFalse(is_palindrome('ComputaciOn'))
        self.assertFalse(is_palindrome('El mejor momento del día es ahora'))


unittest.main()