import unittest


class TestStringReversal(unittest.TestCase):
    def test(self):
        input = "Rosa are red and I am glad"
        expected_result = "glad am I and red are Rosa"
        output = self.reversed_string(input)
        self.assertEqual(expected_result, output)

    def reversed_string(self, input: str):
        return ' '.join(list(reversed(input.split())))


if __name__ == '__main__':
    unittest.main()
