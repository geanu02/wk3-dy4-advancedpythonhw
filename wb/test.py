import unittest

from whiteboard import count_words

class Test_Count_Words(unittest.TestCase):

    def test_simple_string(self):
        result = count_words('to be or not to be')
        expected_output = {'to': 2, 'be': 2, 'or': 1, 'not': 1}
        self.assertEqual(result, expected_output)
        self.assertNotEqual(result, {'to', 1})

    def test_contractions(self):
        self.assertEqual(count_words("'to'f dk dk ' to, DK f f 'TO"), {'to': 3, 'f': 3, 'dk': 3})
    

    def test_punctuation(self):
        self.assertEqual(count_words("to be or not to be?"), {'to': 2, 'be': 2, 'or': 1, 'not': 1})

# if this file is being ran:
if __name__ == '__main__':
    unittest.main()
