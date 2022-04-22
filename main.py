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
  
  




