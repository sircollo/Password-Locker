import random
import string
from user import User
class Credentials:
  '''
  Credentials class to generate new instances of user credentials
  '''
  credentials_list = []
  @classmethod
  def verify_user(cls,user_name,password):
    '''
    verify_user method to check if the user exists in the user_list
    '''
    this_user = ''
    for user in User.user_list:
      if(user.user_name == user_name and user.password == password):
        this_user = user.user_name
        
    return this_user
  def __init__(self,account,account_user_name,account_password):
    '''
    init method that defines user credentials
    '''
    self.account = account
    self.account_user_name = account_user_name
    self.account_password = account_password
    
  def save_credentials(self):
    '''
    save credentials method to save new credentials to credentials list
    '''
    Credentials.credentials_list.append(self)
    
  def delete_credentials(self):
    '''
    delete_credentials method to delete credentials from crdentials list
    '''
    Credentials.credentials_list.remove(self)
    
  @classmethod
  def find_credentials_by_account_name(cls, account):
    '''
    method that searches for credentials by account name and returns details
    '''
    
    for credential in cls.credentials_list:
      if credential.account == account:
        return credential
  @classmethod
  def is_available(cls,account):
    '''
    method to check if credentials exist
    '''
    for credential in cls.credentials_list:
      if credential.account == account:
        return True
    return False
  @classmethod
  def display_various_credentials(cls):
    '''
    display method that returns all saved credentials of a user
    '''
    return cls.credentials_list
  
  #password generator  
  
  def generate_random_password():
    '''
    method to generate random password for user using character strings, numbers and symbols
    '''
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    length = int(input("Enter password length: "))
    random.shuffle(characters)
    password = []
    for i in range(length):
      password.append(random.choice(characters))
      
    random.shuffle(password)
    # password = 
    return (''.join(password))