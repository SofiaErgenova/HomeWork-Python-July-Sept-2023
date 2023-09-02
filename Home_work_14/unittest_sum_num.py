from task_2 import sum_nums
import unittest

class TestCaseSumNum(unittest.TestCase):
    '''Тестирование функции sum_nums, которая возвращает сумму чисел между между переданными индексами.'''

    def test_1(self):
        self.assertEqual(sum_nums([1, 2, 3, 4, 5], 1, 4), 7)

    def test_2(self):
        self.assertEqual(sum_nums([1, 2, 3, 4, 5], 1, 10), 12)

    def test_3(self):
        self.assertEqual(sum_nums([1, 2, 3, 4, 5], -1, 4), 10)  

    def test_4(self):
        self.assertEqual(sum_nums([1, 2, 3, 4, 5], 1, 1), 0)  


if __name__ == '__main__':
    unittest.main(verbosity=2)
