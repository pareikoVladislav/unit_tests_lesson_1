import unittest


def test_loader():
    loader = unittest.TestLoader()

    group = loader.discover('.', pattern="test_*.py")

    runner = unittest.TextTestRunner()
    runner.run(group)


if __name__ == '__main__':
    test_loader()
