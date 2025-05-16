import pytest

from example01.calculator import sum, sub, mul, div

def test_sum():
    assert sum(1, 2) == 3
    
def test_sub():
    assert sub(1, 2) == -1
    
def test_mul():
    assert mul(1, 2) == 2
    
def test_div():
    assert div(1, 2) == 0.5
    
def test_div_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        div(1, 0)