#!/usr/bin/env python3.8

from user import User
from credentials import Credentials


def create_new_user(user_name, password):
  '''
  Function to create new user
  '''
  new_user = User(user_name, password)
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


def login_user(user_name, password):
  authenticate_user = Credentials.verify_user(user_name, password)
  return authenticate_user


def create_new_credentials(account, account_user_name, password):
    """
    Function to create new user credentials
    """
    new_credentials = Credentials(account, account_user_name, password)
    return new_credentials


def save_credentials(credentials):
    '''
    Funtion to save new user credentials
    '''
    credentials.save_credentials()


def find_credential(account):
    """
    Function to search an account name in credentials list
    """
    return Credentials.find_credentials_by_account_name(account)


def display_various_accounts():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_various_credentials()


def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """
    credentials.delete_credentials()


def landing():
    print("         ********          *            ***********       *********       *        *            ")
    print("         *      *          *            *         *       *        *      *       *             ")
    print("         *      *          *            *  *****  *       *               *      *              ")
    print("         *******           *            *  *   *  *       *               *   *                 ")
    print("         *        ******   *            *  *****  *       *               *   *                 ")
    print("         *                 *            *         *       *         *     *      *              ")
    print("         *                 *********    ***********       **********      *        *            ")


landing()


def main_function():
    print("Welcome to the best password locker!\nChoose an option below to conitune")
    print(f"RA --- Register Account \nLI --- Login In")
    short_code = input().lower().strip()
    if short_code == 'ra':
      print("Register here...")
      print("="*50)
      user_name = input("User name: ")
      while True:
          print(
              "Choose password type:\nCP---Enter Custom Pasword\nGP---Use Generated Password")
          password_type = input().lower().strip()
          if password_type == 'cp':
              password = input("Enter Password\n")
              break
          elif password_type == 'gp':
              password = generate_random_password()
              break
          else:
              print("Invalid option")

      add_user(create_new_user(user_name, password))
      # print(str(password))
      print("="*50)
      print(
          f"Account Created Successfully!\nUsername:{user_name}\nPassword:{password}")
      print("="*50)
    #   return login_user(user_name,password)
      print("Use these short codes to continue...\nNC --- New Credentials \nFC --- Find a credential \nVC --- View Credentials \nDel--- Delete account credential \nQ  --- Quit application \n")
      short_code = input().lower().strip()

    elif short_code == "li":
        print("Login here...")
        user_name = input("Enter Username: ")
        password = input("Enter Password: ")
        login = login_user(user_name, password)
        if login_user == login:
          print("Login Successfull")
          print(f"{user_name}, Continue to lock your credentials")
        else:
            print("You have not registered, Please enter username and password:")
            user_name = input("Enter Username: ")
            password = input("Enter Password: ")
            while True:
                print(
                    "Choose password type:\nCP---Enter Custom Pasword\nGP---Use Generated Password")
                password_type = input().lower().strip()
                if password_type == 'cp':
                    password = input("Enter Password\n")
                    break
                elif password_type == 'gp':
                    password = generate_random_password()
                    break
                else:
                    print("Invalid option")

            add_user(create_new_user(user_name, password))
            # print(str(password))
            print("="*50)
            print(
                f"Account Created Successfully!\nUsername:{user_name}\nPassword:{password}")
            print("="*50)

    while True:
        print("Use these short codes to continue...\nNC --- New Credentials \nFC --- Find a credential \nVC --- View Credentials \nDel--- Delete account credential \nQ  --- Quit application \n")
        short_code = input().lower().strip()
        if short_code == "nc":
            print("Create New Credentials")
            print("="*20)
            print("Account name: ")
            account = input().lower()
            print("Account's username: ")
            account_user_name = input()
            while True:
                print(
                    "Choose password Type...\nCP---Enter Custom Password\nGP---Use Generated Password")
                password_type = input().lower().strip()
                if password_type == 'cp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_type == 'gp':
                    password = generate_random_password()
                    break
                else:
                    print("Invalid Option!")

            save_credentials(create_new_credentials(
                account, account_user_name, password))
            print('\n')
            print("*"*40)
            print(
                f"Account Credential saved successfully!\nAccount: {account} \nUsername: {account_user_name}\nPassword: {password}")
            print("*"*40)
        elif short_code == "fc":
            print("Enter the Account Name you want to search")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 40)
                print(
                    f"User Name: {search_credential.account_user_name} \nPassword : {search_credential.account_password}")
                print('-' * 40)
            else:
                print("Credentials not found")
        elif short_code == "vc":
            if display_various_accounts():
                print("Your saved accounts: ")
                print('=' * 40)

                for account in display_various_accounts():
                    print(
                        f"Account: {account.account} \nUsername: {account_user_name}\nPassword: {account.account_password}")
                    print('*' * 40)
            else:
                print("No Credentails saved...")
                print("\n")

        elif short_code == "del":
            print("Enter account name to delete:")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("-"*40)
                search_credential.delete_credentials()
                print('\n')
                print(f"{search_credential.account} successfully deleted!")
                print('\n')
            else:
                print("Account to delete not found")
                print("="*40)
        elif short_code == 'q':
            print("Are you sure you want to quit?")
            print("Y - to quit application N- to continue")
            short_code = input().strip().lower()
            if short_code == "y":
                break
            else:
                continue
        else:
            print("Invalid option, Please choose from the options below")
    else:
        print("Invalid option!, Choose an item below")
        main_function()


if __name__ == "__main__":
  main_function()
