import unittest
from Sort import *

from app import sort_numbers

class TestApp(unittest.TestCase):    
                       
    def test_app(self):   
            self.assertTrue(sort_numbers())
          
if __name__ == '__main__':
    unittest.main()