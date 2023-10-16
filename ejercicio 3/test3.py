import unittest
from ejercicio3 import minimum_jumps


class TestExercise3(unittest.TestCase):

    """
    This test check if the result of the function of minium_jumps not change the results.
    """
    def test_minimum_jumps(self):
        minmun_jump_one = minimum_jumps(7)
        minmun_jump_two = minimum_jumps(19)
        minmun_jump_three = minimum_jumps(65)
        minmun_jump_four = minimum_jumps(90)
        minmun_jump_five = minimum_jumps(37)

        self.assertNotEqual(minmun_jump_one, 3.99)
        self.assertNotEqual(minmun_jump_two, 8)
        self.assertNotEqual(minmun_jump_three, 12.00000001)
        self.assertNotEqual(minmun_jump_four, 5)
        self.assertNotEqual(minmun_jump_five, -9)
        
unittest.main()