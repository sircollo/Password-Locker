class User:
  '''
  Class that generates new instances of a user
  '''
  
  user_list = []
  def __init__(self,user_name,password):
    self.user_name = user_name
    self.password = password