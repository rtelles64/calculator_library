"""
Unit tests for the calculator library.
"""

import calculator


class TestCalculator:
    '''
    Class to test calculator library.
    '''
    def test_addition(self):
        '''
        Tests addition function.
        '''
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        '''
        Tests subtraction function.
        '''
        assert 2 == calculator.subtract(4, 2)
