import sys
import unittest


def power(a: int, b: int) -> int:
    """
    Занимается возведением в степень одного числа на другое
    :param a: int: первое число
    :param b: int: второе число
    :return: int: результат возведения в степень
    """
    return a ** b


class TestPowerFunction(unittest.TestCase):
    """
    Этот класс тестирует функцию возведения в степень одного числа на другое
    """

    def test_power_with_positive_numbers(self):
        """
        Тестирует возведение в степень двух пятёрок
        :return: Ture | False
        """
        self.assertEqual(power(5, 5), 3125)


if __name__ == '__main__':
    runner = unittest.TextTestRunner(
        stream=sys.stderr,
        verbosity=2,
        descriptions=True,
        buffer=False
    )

    runner.run(test=TestPowerFunction('test_power_with_positive_numbers'))
