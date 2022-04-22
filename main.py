#!/usr/bin/env python3.8

from user import User
from credentials import Credentials

def create_new_user(user_name,password):
  '''
  Function to create new user
  '''
  new_user = User(user_name,password)
  return new_user

def add_user(user):
  '''
  Function to add a new user
  '''
  user.add_user()

def display_user():
  '''
  Funtion to display a user
  '''
  return User.display_user()

def generate_random_password():
  random_password = Credentials.generate_random_password()
  return random_password

def login_user(user_name,password):
  authenticate_user = Credentials.verify_user(user_name,password)
  return authenticate_user

def main_function():
  print("Hi there, What is your name?")
  userName = input()
  print(f"Hi, {userName}. Welcome to the best password locker!\nChoose an option below...")
  print(f"RA --- Register Account \nLI --- Login In")
  short_code = input().lower().strip()
  if short_code == 'ra':
    print("Register here...")
    print("="*50)
    user_name = input("User name: ")
    while True:
      print("Choose password type:\nCP---Enter Custom Pasword\nGP---Use Generated Password")
      password_type = input().lower().strip()
      if password_type == 'cp':
         password = input("Enter Password\n")
         break
      elif password_type == 'gp':
         password = generate_random_password()
         break
      else:
         print("Invalid option")
        
        
    add_user(create_new_user(user_name,password))
    # print(str(password))
    print("="*50)
    print(f"Account Created Successfully!\nUsername:{user_name}\nPassword:{password}")
    print("="*50)
    
  elif short_code == "li":
    print("Login here...")
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    login = login_user(user_name,password)
    if login_user == login:
      print(f"{user_name}, Continue to lock your credentials")
      
    
    
if __name__=="__main__":
  main_function()

  
