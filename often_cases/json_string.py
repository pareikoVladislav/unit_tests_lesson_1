import json
import unittest


def parse_json_string(data: str) -> dict:
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON data")


class TestParseJSON(unittest.TestCase):
    def setUp(self):
        self.valid_json = '''
        [
            {
                "pk": 1,
                "name": "Мистика"
            },
            {
                "pk": 2,
                "name": "Биография"
            },
            {
                "pk": 3,
                "name": "Ужасы"
            },
            {
                "pk": 4,
                "name": "Детектив"
            }
        ]
        '''
        self.single_object = '''{"pk": 5, "name": "Романы"}'''
        self.empty_json = '{}'
        self.empty_array_json = '[]'
        self.bad_json = 'bad JSON'
        self.nested_data = '''{
           "pk": 1,
           "details": {
               "description": "A detailed description",
               "metadata": {
                   "created": "2023-06-23",
                   "modified": "2023-06-24"
               }
           },
           "tags": ["fiction", "mystery", "thriller"]
       }
       '''

    def test_valid_json(self):
        result = parse_json_string(self.valid_json)[0]
        self.assertEqual(
            result,
            {"pk": 1, "name": "Мистика"}
        )
        self.assertIsInstance(parse_json_string(self.valid_json), list)

    def test_invalid_json(self):
        self.assertRaises(ValueError, parse_json_string, self.bad_json)

    def test_empty_object_json(self):
        self.assertEqual(parse_json_string(self.empty_json), {})

    def test_empty_array_json(self):
        self.assertEqual(parse_json_string(self.empty_array_json), [])

    def test_nested_data_json(self):
        parsed_data = parse_json_string(self.nested_data)

        self.assertIsInstance(parsed_data, dict)
        self.assertIn('details', parsed_data)
        self.assertIn('tags', parsed_data)
        self.assertIsInstance(parsed_data['details'], dict)
        self.assertIsInstance(parsed_data['tags'], list)

    def tearDown(self):
        del self.valid_json
        del self.single_object
        del self.empty_json
        del self.empty_array_json
        del self.bad_json


if __name__ == '__main__':
    unittest.main()
