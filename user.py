class User:
  '''
  Class that generates new instances of a user
  '''
  
  user_list = []
  def __init__(self,user_name,password):
    self.user_name = user_name
    self.password = password
    
  def add_user(self):
    '''
    add_user method to save new user to user_list
    '''
    User.user_list.append(self)
    
  @classmethod
  def display_user(cls):
    '''
    method to display user from user list
    '''
    return cls.user_list
    
    
  def delete_user(self):
    '''
    delete_user method to delete user details from list
    '''
    User.user_list.remove(self)
    

      