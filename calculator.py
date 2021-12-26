# This app is designed per the Real Python tutorial below:
#   https://realpython.com/python-continuous-integration/

"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    '''
    Adds terms together.

    Parameters
    ----------
    first_term : int, float
        The first term to add
    second_term : int, float
        The second term to add

    Returns
    -------
    int, float
        The result of the addition
    '''
    return first_term + second_term


def subtract(first_term, second_term):
    '''
    Subtracts terms from each other.

    Parameters
    ----------
    first_term : int, float
        The term to subtract from
    second_term : int, float
        The term to subtract

    Returns
    -------
    int, float
        The result of the subtraction
    '''
    return first_term - second_term
