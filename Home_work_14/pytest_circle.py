import pytest
from task_1 import Circle



def test_length_circle():
    assert Circle.length_circle(Circle(5)) == 31.41592653589793

def test_square_circle():
     assert Circle.square_circle(Circle(5)) == 78.53981633974483


if __name__ == '__main__':
    pytest.main(['-v'])