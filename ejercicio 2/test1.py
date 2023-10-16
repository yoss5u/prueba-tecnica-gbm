import unittest
from ejercicio2 import calculate_points

class TestCalculatePoints(unittest.TestCase):

    """
    This test confirm the result of the function that make the operations to assign the points. 

    We have to create the result of one race and the punctuation system. Also we have to know the result of the champions to confirm the result.
    """
    def test_calcualtePoints(self):
        results = [[3, 2, 1]]
        system_punctuation = [3, 5, 3, 2]
        points = calculate_points(results, system_punctuation)
        self.assertEqual(points, [2, 3, 5])

unittest.main()