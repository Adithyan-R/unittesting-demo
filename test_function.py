import unittest

from function import *
class TestAverage(unittest.TestCase):
    
    def test_average(self):
        res=average([10,10,10])
        self.assertEqual(res,10,'Failed value not match')

        '''
        This test case will pass 
        
        '''
        
    def test_max(self):
        
        res=maximum([10,12,14])##act
       
        self.assertEqual(res,12)##assert
        '''
        This test case will fail

        '''


        

if __name__ == "__main__":
    unittest.main()

        
