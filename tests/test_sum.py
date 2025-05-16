from example01 import sum

def test_sum():
    assert sum(1, 2) == 3
    
def test_sum_negatives():
    assert sum(-2, -3) == -5
    
def test_sum_zero():
    assert sum(0, 0) == 0