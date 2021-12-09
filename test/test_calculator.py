import unittest
from calculator import calculateTip, calculateTotal

class TestCalculator(unittest.TestCase):

    def test_should_calculate_10_percent_tip(self):
        amount = 100
        percentage = 0.1
        tip = calculateTip(amount, percentage)
        self.assertEqual(tip, 10)

    def test_should_calculate_15_percent_tip(self):
        amount = 100
        percentage = 0.15
        tip = calculateTip(amount, percentage)
        self.assertEqual(tip, 15)
    
    def test_should_calculate_20_percent_tip(self):
        amount = 100
        percentage = 0.20
        tip = calculateTip(amount, percentage)
        self.assertEqual(tip, 20)

    def test_should_calculate_total(self):
        amount = 100
        percentage = 0.1
        total = calculateTotal(amount, percentage)
        self.assertEqual(total, 110)


if __name__ == '__main__':
    unittest.main()


