from calculator_manual_testing import square
import pytest # dont need to import for  running tests, but because we wanted to use .raises function of pytest module 

def test_positive():
    assert square(2) == 4
    assert square(-2) == 4

def test_negative():
    assert square(3) == 9
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

# to use pytest- put in terminal "pytest filename.py"