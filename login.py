import json
from validations import isUsernameExist, isPasswordTrue
from databaseConfig import *
from account import PageRouter


def GetUsername():
    userName = input("- Enter your username: ")
    while(not isUsernameExist(userName, True)):
        userName = input("- Enter your username: ")
    return userName     


def GetPassword(argUsername):  
    password = input("- Enter your password: ")
    while(not isPasswordTrue(password, argUsername)):
        password = input("- Enter your password: ")
    return True    
  

#login entry point
def Login():
    print("""
Welcome To Log in Page!
To login, please Enter your credentials:
        """)
    username = GetUsername()

    if(GetPassword(username)):
        PageRouter(username)
    
    