'''
Created on 29 ago. 2017

@author: Val
'''
import unittest
from pyGeni import profile
import os


class Test(unittest.TestCase):


    def setUp(self):
        #We used the sandbox here
        self.stoken = os.environ['SANDBOX_KEY']
        profile.s.update_geni_address("https://www.sandbox.geni.com")
        profile.s.VERIFY_INPUT = False

    def testName(self):
        '''
        Test reading a profile in sandbox
        '''
        prof = profile.profile("1149101", self.stoken)
        assert( "Testing" in prof.nameLifespan())
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()