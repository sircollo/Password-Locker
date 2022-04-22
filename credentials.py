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