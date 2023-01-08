import unittest
import json
from Sort import *

from app import sort_numbers

f = open('numbers.json')
data = json.load(f)


class TestApp(unittest.TestCase):    
           
    def test_json_only_int(self):
        for number in data['numbers']:        
            self.assertEqual(type(number),int)
            
    def test_json_more_one_value(self):      
            self.assertNotEqual(len(data["numbers"]),0)
            self.assertNotEqual(len(data["numbers"]),1)
            
    def test_app(self):   
            self.assertTrue(sort_numbers())
          
if __name__ == '__main__':
    unittest.main()