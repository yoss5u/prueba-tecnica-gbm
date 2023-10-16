import unittest
from unittest.mock import patch
from ejercicio2 import obtain_results

class TestObtainResults(unittest.TestCase):
    
    """
    This test confirm that the results of each GranPrix work exactly
    """

    def test_obtain_result(self):
        input_values = ['1 2 3\n', '3 2 1\n']
        expected_output = [[1, 2, 3], [3, 2, 1]]
        with patch('builtins.input', side_effect=input_values):
            result = obtain_results(2)
            self.assertEqual(result, expected_output)

unittest.main()
