import unittest as ut

from google.genai.caches import Caches

from Calculations import Calculations

class TestCalculations(ut.TestCase):

    def test_sum(self):
        calculation = Calculations(4, 2)
        self.assertEqual(calculation.get_sum(), 6, 'The sum is wrong.')
        self.assert
    def test_diff(self):
        calculation = Calculations(4, 2)
        self.assertEqual(calculation.get_difference(), 2, 'The diff is wrong')

    def test_sqrt(self):
        calculation = Calculations(35, 0).get_sqrt()

        self.assertEqual(calculation*calculation, 35 , "sqrt is wrong")

if __name__ == '__main__':
    ut.main()