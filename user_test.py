import unittest
from user import User

class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for user class methods.
  
  Args:
  unittest.TestCase: TestCase class that helps in creating test cases.
  '''
  def setUp(self):
    '''
    set up method to run before each test case
    '''
    self.new_user = User("admin","12345678")
    
  def test_init(self):
    '''
    test_init case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.user_name,"admin")
    self.assertEqual(self.new_user.password,"12345678")
    

if __name__=="__main__":
  unittest.main()