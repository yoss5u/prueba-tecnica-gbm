import unittest
from main import realice_prediction

class TestPredictionModel(unittest.TestCase):

    def test_prediction_high(self):
        prediction = realice_prediction(1525, 25)
        self.assertEqual(prediction, [3])

    def test_prediction_low(self):
        prediction = realice_prediction(779, 10)
        self.assertEqual(prediction, [1]) 

    def test_prediction_with_medium(self):
        prediction = realice_prediction(1122, 15)
        self.assertEqual(prediction, [2])


unittest.main()