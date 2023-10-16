import unittest
from ejercicio2 import obtain_g_and_p

class TestObtainGAndP(unittest.TestCase):

    """
    This test confirm that the function that receives the number of GrandPrix and the total of runners
    """

    def tes_g_and_p(self):
        input_values = ['3 10\n', '0 0\n']
        expected_output = [(3, 10), (0, 0)]
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            for expected in expected_output:
                result = obtain_g_and_p()
                self.assertEqual(result, expected)

unittest.main()