import unittest
from credentials import Credentials

class TestCase(unittest.TestCase):
  '''
  Test class that defines credentials test case methods.
  '''
  def setUp(self):
    '''
    Method to run before each test case
    '''
    self.new_credentials = Credentials("Facebook","collos","fbpassword")
  
  def test_init(self):
    '''
    Test case to test if new credentials are initialized properly
    '''
    self.assertEqual(self.new_credentials.account,"Facebook")
    self.assertEqual(self.new_credentials.account_user_name,"collos")
    self.assertEqual(self.new_credentials.account_password,"fbpassword")
    
if __name__=="__main__":
  unittest.main()
    