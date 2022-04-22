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
    
  def test_add_user(self):
    '''
    test case to test if a new user instance is added into the user list
    '''
    self.new_user.add_user()
    self.assertEqual(len(User.user_list),1)
    
  def test_delete_user(self):
    '''
    test_delete_user method to check if user details can be deleted from list
    '''
    self.new_user.add_user()
    self.new_user.delete_user()
    self.assertEqual(len(User.user_list),1)
    

if __name__=="__main__":
  unittest.main()