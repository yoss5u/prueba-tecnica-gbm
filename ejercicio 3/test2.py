import unittest
from ejercicio3 import minimum_jumps


class TestExercise3(unittest.TestCase):

    """
    This test check if the value to reach the minium jumps is less than 106
    """

    def test_minimum_jumps(self):
        self.assertFalse(minimum_jumps(107))
 
        
unittest.main()