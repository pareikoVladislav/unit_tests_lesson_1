import unittest


def add_to_dict(d, key, value):
    if not isinstance(d, dict):
        raise TypeError("First argument must be a dictionary")
    if not isinstance(key, (str, int, float, bool)):
        raise TypeError("Key must be a string, integer, float, or boolean")
    if key not in d:
        d[key] = value
    else:
        return d[key]

    return d


class TestDictGetOrCreate(unittest.TestCase):
    # def setUpClass(cls):
    #     ...
    #
    # def tearDownClass(cls):
    #     ...

    def setUp(self):
        self.test_dict = {'a': 21}
        self.test_new_key = 'b'
        self.test_new_value = "HELLO"
        self.existing_key = 'a'
        self.existing_value = 21
        self.bad_dict = "NOT A DICT"
        self.bad_key = []

    def test_add_to_dict_new_key(self):
        result = add_to_dict(
            self.test_dict,
            self.test_new_key,
            self.test_new_value
        )

        self.assertEqual(result, {'a': 21, 'b': "HELLO"})

    def test_take_bad_dict(self):
        self.assertRaises(
            TypeError,
            add_to_dict,
            self.bad_dict,
            self.existing_key,
            self.existing_value
        )

    def test_bad_key(self):
        self.assertRaises(
            TypeError,
            add_to_dict,
            self.test_dict,
            self.bad_key,
            self.test_new_value
        )

    def test_add_valid_keys(self):
        test_cases = [
            ({}, 'key_str', 'value'),
            ({}, 42, 'value'),
            ({}, 3.14, 'value'),
            ({}, True, 'value'),
        ]
        for d, key, value in test_cases:
            with self.subTest(d=d, key=key, value=value):
                result = add_to_dict(d, key, value)
                self.assertEqual(result[key], value)

    def tearDown(self):
        del self.test_dict
        del self.test_new_key
        del self.test_new_value
        del self.bad_dict
        del self.bad_key
        del self.existing_key
        del self.existing_value


if __name__ == '__main__':
    unittest.main()
