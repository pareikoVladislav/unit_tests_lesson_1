import unittest


# def add(a, b):
#     try:
#         return a + b
#     except TypeError:
#         raise TypeError('error')

def add(a, b):
    # try:
    return a + b
    # except TypeError:
    #     raise TypeError('error')


class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(add(8, 0), 8)

    def test_add_negative(self):
        self.assertEqual(add(-1, 0), -1)

    def test_add_int_and_string(self):
        self.assertRaises(TypeError, add, 5, "qwerty")


# if __name__ == '__main__':
#     unittest.main()
