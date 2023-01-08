import unittest
from numbers import numbers




class TestApp(unittest.TestCase):
    def test_int(self):
        result = False
        for number in numbers:
            if type(number) != int : 
                result = True

        self.assertEqual(result,False)
    def test_single_number(self):
        result = False
        for number in numbers:
            if len(numbers) <= 1 : 
                result = True

        self.assertEqual(result,False)
          
if __name__ == '__main__':
    unittest.main()