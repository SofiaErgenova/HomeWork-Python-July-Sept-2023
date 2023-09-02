import pytest
from task_2 import sum_nums

def test_1():
    assert sum_nums([1, 2, 3, 4, 5], 1, 4) == 7

def test_2():
    assert sum_nums([1, 2, 3, 4, 5], 1, 10) ==  12

def test_3():
    assert sum_nums([1, 2, 3, 4, 5], -1, 4) == 10  

def test_4():
    assert sum_nums([1, 2, 3, 4, 5], 1, 1) == 0  



if __name__ == '__main__':
    pytest.main(['-v'])

