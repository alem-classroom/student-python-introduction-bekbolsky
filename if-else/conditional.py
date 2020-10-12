import random


def is_positive(num):
    """
    return true if num is positive, otherwise return false
    """
    if num > 0:
        return True
    else:
        return False


def is_even(num):
    """
    return true if num is even, otherwise return false
    """
    if num % 2 == 0:
        return True
    else:
        return False


def is_positive_and_even(num):
    """
    return true if num is positive and even, otherwise return false
    """
    if num > 0 and num % 2 == 0:
        return True
    else:
        return False


def is_positive_or_even(num):
    """
    return true if num is positive or even, otherwise return false
    """
    if num > 0 or num % 2 == 0:
        return True
    else:
        return False


def test_conditional():
    assert is_positive(5) == True
    assert is_positive(-5) == False
    assert is_even(10) == True
    assert is_even(5) == False
    assert is_positive_and_even(10) == True
    assert is_positive_and_even(5) == False
    assert is_positive_or_even(1) == True
    assert is_positive_or_even(2) == True
    assert is_positive_or_even(-1) == False
