import unittest
from ejercicio3 import minimum_jumps


class TestExercise3(unittest.TestCase):

    """
    This test confirm the results of diferent values 
    """

    def test_minimum_jumps(self):
        minmun_jump_one = minimum_jumps(7)
        minmun_jump_two = minimum_jumps(19)
        minmun_jump_three = minimum_jumps(65)
        minmun_jump_four = minimum_jumps(90)
        minmun_jump_five = minimum_jumps(37)

        self.assertEqual(minmun_jump_one, 4)
        self.assertEqual(minmun_jump_two, 6)
        self.assertEqual(minmun_jump_three, 12)
        self.assertEqual(minmun_jump_four, 14)
        self.assertEqual(minmun_jump_five, 9)
        
unittest.main()