import pytest
# accepting capitalization: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('rihanna') == 'Rihanna'