import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a * b


class TestCalculatorAdd(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        test_cases = [
            (1, 2, 3),
            (3, 4, 5),
            (0, 0, 5),
            (-1, 1, 0),
        ]

        # for param1, param2, expected in test_cases:  # если хоть один случай упадёт - остальные оставшиеся не отработают
        #     self.assertEqual(calc.add(param1, param2), expected)


        # даже если хоть один упадёт - отработает до конца, потом выведет ошибки
        # for param1, param2, expected in test_cases:
        #     with self.subTest(param1=param1, param2=param2, expected=expected):
        #         self.assertEqual(calc.add(param1, param2), expected)


# class TestCalculatorAdd(unittest.TestCase):
#
#     def test_add(self):
#         calc = Calculator()
#         self.assertEqual(calc.add(2, 3), 5)
#         self.assertEqual(calc.add(-1, -2), -3)
#         self.assertEqual(calc.add(10, 0), 10)
#         self.assertRaises(TypeError, calc.add, None, None)


class TestCalculatorSubtract(unittest.TestCase):
    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(2, 3), 6)
        self.assertEqual(calc.subtract(-1, -2), 2)
        self.assertEqual(calc.subtract(10, 0), 0)
        self.assertRaises(TypeError, calc.subtract, None, None)


def suite():
    group_suite = unittest.TestSuite()

    # group_suite.addTest(TestCalculatorAdd('test_add'))
    # group_suite.addTest(TestCalculatorSubtract('test_subtract'))

    group_suite.addTest(unittest.makeSuite(TestCalculatorSubtract))
    group_suite.addTest(unittest.makeSuite(TestCalculatorAdd))

    return group_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
