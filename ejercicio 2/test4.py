import unittest
from unittest.mock import patch
from ejercicio2 import obtain_scoring_system

class TestObtainScoringSystem(unittest.TestCase):

    """
    This test confirm that make the operations well to asign the correct champion or champions.
    """

    def test_scoring_system(self):
        input_values = ['2\n', '5 5 4 3 2 1\n', '3 10 5 1\n']
        expected_output = [[1, 2, 3], [1, 3]]
        with patch('builtins.input', side_effect=input_values):
            results = [[1, 2, 3], [3, 2, 1]]
            champions_by_system = obtain_scoring_system(results)
            self.assertEqual(champions_by_system, expected_output)

unittest.main()