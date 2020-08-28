from validations import *
import json


class User:
    def __init__(self, argName, argLastName, argUsername, argPassword, argUserType):
        self.name = argName
        self.lastName = argLastName
        self.username = argUsername        
        self.password = argPassword
        self.type =  argUserType
        self.AddToBase()
        
    def AddToBase(self):
        dataDict = {}
        dataDict["username"] = self.username
        dataDict["name"] = self.name
        dataDict["lastName"] = self.lastName
        dataDict["password"] = self.password
        dataDict["type"] = self.type
        

        dataList = GetDataFromJson("database.json")
        dataList.append(dataDict)
        
        SetDataToJson("database.json", dataList)


def GetName():
    name = input("- Enter your name: ")
    while(not isValidName(name)):
        name = input("- Enter your name: ")
    return name


def GetLastName():
    lastName = input("- Enter your last name: ")
    while(not isValidLastName(lastName)):
        lastName = input("- Enter your last name: ")
    return lastName
 

def GetUserName():
    userName = input("- Enter your username: ")
    while(not isValidUsername(userName)):
        userName = input("- Enter your username: ")
    return userName


def GetUserPassword():   
    print("Tip: Password should contain: letters(upper, lower), symbols and numbers.")
    password = input("- Enter your password: ")
    while(not isValidPassword(password)):
        password = input("- Enter your password: ")

    # Confirm Password
    confirmPassword = input("- Confirm password: ")
    while(not isValidConfirmPassword(password, confirmPassword)):
         confirmPassword = input("- Confirm password: ")
    return password


def GetAccountType():
    def isValidType(argText):
        if(account == "admin"):
            return True
        else:
            if(account == "editor"):
                return True
            else:
                print("Attention: This type doesn't exist!\n")  
                return False      
    
   
    account = input()
    while(not isValidType(account)):
        account = input()
    return account


# Register entry point
def Register():
    print("""
Welcome To Registration Page!
To register, please Enter your datas:
    """)
    inpName = GetName()
    inpLastName = GetLastName()
    inpUserName = GetUserName()
    inpPassword = GetUserPassword()
    print("""
Choose Your account type:
- Admin (type: admin)
- Coordinator (type: editor) """)
    accType = GetAccountType()
    print()

    User(inpName, inpLastName, inpUserName, inpPassword, accType)
    print("You account successfully added to Data Base.\n")


