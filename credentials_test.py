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
    
  def tearDown(self):
    '''
    tearddown method to clean up after each test case has been run
    '''
    Credentials.credentials_list = []  
  
  def test_save_credentials(self):
    '''
    Test case to check if credentials are saved in credentials list
    '''
    self.new_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)  
  
    
  def test_save_multiple_accounts(self):
    '''
    test method to check if we can save multiple accounts
    '''
    self.new_credentials.save_credentials()
    test_credentials = Credentials("Gmail","sircollo","078jjyY76")
    test_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),2)
  
  def test_delete_credentials(self):
    '''
    method to test if credentials can be deleted
    '''
    self.new_credentials.save_credentials()
    test_credentials = Credentials("Gmail","sircollo","078jjyY76")
    test_credentials.save_credentials()
    
    self.new_credentials.delete_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)
    
  def test_find_credentials_by_account_name(self):
    '''
    test to check if we can find account credetials by account name and display information
    '''
    self.new_credentials.save_credentials()
    test_credentials = Credentials("Gmail","sircollo","078jjyY76")
    test_credentials.save_credentials()
    
    found_credentials = Credentials.find_credentials_by_account_name("Gmail")
    self.assertTrue(found_credentials.account,test_credentials.account)
    
  def test_credentials_available(self):
    '''
    method to check if credentials of an account actually exists
    '''
    self.new_credentials.save_credentials()
    found_credentials = Credentials("Gmail","sircollo","078jjyY76")
    found_credentials.save_credentials()
    is_found = Credentials.is_available("Gmail")
    # self.assertEqual(is_found,"Gmail")
    
  def test_display_various_credentials(self):
    '''
    test case method to check if all credentials saved by a user can be displayed
    '''
    self.assertEqual(Credentials.display_various_credentials(),Credentials.credentials_list)
    
    
  
    
if __name__=="__main__":
  unittest.main()
    