import unittest

from app import sort_numbers

class TestApp(unittest.TestCase):    
    def setUp(self):
        print('- Test verileri hazırlanıyor...')
        self.numbers = [5,1,8,7]
        print(self.numbers)
    def tearDown(self):
        print('- Test verileri siliniyor...')
        self.numbers = []
                       
    def test_app(self):
            
            self.assertTrue(sort_numbers(self.numbers))

          
if __name__ == '__main__':
    unittest.main()