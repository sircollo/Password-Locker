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
      