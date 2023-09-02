
from task_1 import Circle
import unittest

class TestCaseCircle(unittest.TestCase):
    '''Тестирование функций класса Circle'''

    def test_length_circle(self):
        self.assertEqual(Circle.length_circle(Circle(5)), 31.41592653589793)


    def test_square_circle(self):
        self.assertEqual(Circle.square_circle(Circle(5)), 78.53981633974483)

if __name__ == '__main__':
    unittest.main(verbosity=2)

