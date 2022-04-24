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

def create_new_credentials(account,account_user_name,password):
    """
    Function to create new user credentials
    """
    new_credentials = Credentials(account,account_user_name,password)
    return new_credentials
  
def save_credentials(credentials):
    '''
    Funtion to save new user credentials
    '''
    credentials.save_credentials()

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
        user_name = input("Enter Username: ")
        password = input("Enter Password: ")
        login = login_user(user_name,password)
        if login_user == login:
          print(f"{user_name}, Continue to lock your credentials")
    while True:
        print("Use these short codes...\nNC --- New Credentials \nFC --- Find a credential \nVC --- View Credentials \nDel--- Delete account credential \nQ  --- Quit application \n")
        short_code = input().lower().strip()
        if short_code == "nc":
            print("Create New Credentials")
            print("="*20)
            print("Account name: ")
            account = input().lower()
            print("Account's username: ")
            account_user_name = input()
            while True:
                print("Choose password Type...\nCP---Enter Custom Password\nGP---Use Generated Password")
                password_type = input().lower().strip()
                if password_type == 'cp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_type == 'gp':
                    password = generate_random_password()
                    break
                else:
                    print("Invalid Option!")
                    
            save_credentials(create_new_credentials(account,account_user_name,password))
            print('\n')
            print("*"*40)
            print(f"Account Credential saved successfully!\nAccount: {account} \nUsername: {account_user_name}\nPassword: {password}")
            print("*"*40)
              
                        
      
    
    
if __name__=="__main__":
  main_function()

  
