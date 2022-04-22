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
  User.add_user()

def display_user():
  '''
  Funtion to display a user
  '''
  return User.display_user()

def main_function():
  print("Hi there, What is your name?")
  userName = input()
  print(f"Hi, {userName}. Welcome to the best password locker!\nChoose an option below...")
  print(f"RA --- Register Account \nLI --- Login In")
  
  
if __name__=="__main__":
  main_function()

  
