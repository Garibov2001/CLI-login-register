import json
from texttable import Texttable
from validations import *
from databaseConfig import *


# usernamein tipine gore uygun sehife oturur
def PageRouter(argUsername):
    for eachDict in GetDataFromJson("database.json"):
            for key,value in eachDict.items():
                if(key == "username" and value == argUsername):
                    for key,value in eachDict.items():
                        if(key == "type"):
                            if(value == "admin"):
                                AdminPage(argUsername)
                                break
                            else:
                                CoordinatorPage(argUsername)
                                break                   


# Admin Page
def AdminPage(argUsername):
    
    # Sehifede olan butun accountlarin datalarini gosterir
    def ShowAccountsData():
        print("All accounts datas:")
        dataArr = [['Name', 'Last name', 'username', 'password','type']]
        for eachDict in GetDataFromJson("database.json"):
            tempArr = []
            for key,value in eachDict.items():
                tempArr.append(value)
            dataArr.append(tempArr)
        t = Texttable()
        t.add_rows(dataArr)
        print(t.draw(), "\n") 

    # Daxil olunan accountun datalarini gosterir
    def ShowYourDatas():
        print("\nYour datas:")
        for eachDict in GetDataFromJson("database.json"):
            for key,value in eachDict.items():
                if(key == "username" and value == argUsername):
                    for key,value in eachDict.items():
                        print(f'{key} -> {value}')     
                    print()
 
    # Acoount datalarini deyismek
    def AccountSettings():
        # inputlarin dogru olub-olmadidigini gosterir
        def isValidInput():
            userInp = input()
            if(userInp == "back" or userInp == "change-name" or 
               userInp == "change-lastname" or userInp == "change-username" or
               userInp == "change-password"):
                return userInp
            else:
                print("Attention: You don't have this ability, please try againt \n")
                isValidInput()
        
        # Adi deyismek :
        def ChangeName(): 
            name = input("\n- Enter your new name: ")
            while(not isValidName(name)):
                name = input("- Enter your new name: ")  

            dataList = GetDataFromJson("database.json")    
            for eachDict in dataList:
                for key, value in eachDict.items():
                    if(key == "username" and value == argUsername):
                        eachDict["name"] = name
            SetDataToJson("database.json", dataList)
            print("\n-Name successfully changed!\n\n")          

        # Soyadi deyismek :
        def ChangeLastname():
            lastName = input("\n-- Enter your new last name: ")
            while(not isValidLastName(lastName)):
                lastName = input("- Enter your new last name: ")

            dataList = GetDataFromJson("database.json")    
            for eachDict in dataList:
                for key, value in eachDict.items():
                    if(key == "username" and value == argUsername):
                        eachDict["lastName"] = lastName
            SetDataToJson("database.json", dataList)
            print("\n-Last name successfully changed!\n\n")

        # Username-i deyismek :
        def ChangeUsername(): 
            userName = input("- Enter your new username: ")
            while(not isValidUsername(userName)):
                userName = input("- Enter your new username: ")

            dataList = GetDataFromJson("database.json")    
            for eachDict in dataList:
                for key, value in eachDict.items():
                    if(key == "username" and value == argUsername):
                        eachDict["username"] = userName
            SetDataToJson("database.json", dataList)
            print("\n-Username successfully changed! (Restart to apply changes)\n\n") 

        #Sifreni deyismek
        def ChangePassword():
            print("\n-Tip: Password should contain: letters(upper, lower), symbols and numbers.")
            password = input("- Enter your new password: ")
            while(not isValidPassword(password)):
                password = input("- Enter your new password: ")

            # Confirm Password
            confirmPassword = input("- Confirm your new password: ")
            while(not isValidConfirmPassword(password, confirmPassword)):
                confirmPassword = input("- Confirm your new password: ")

            dataList = GetDataFromJson("database.json")    
            for eachDict in dataList:
                for key, value in eachDict.items():
                    if(key == "username" and value == argUsername):
                        eachDict["password"] = password
            SetDataToJson("database.json", dataList)
            print("Password successfully changed!")
            

            
        print("\n\n")
        print("You are in account settings, you can do:")
        print("- Go back to profile page (back)")
        print("- Change your name (change-name)")
        print("- Change your last name (change-lastname)")
        print("- Change your username (change-username)")
        print("- Change your password (change-password)")

        getInp = isValidInput()

        if(getInp == "back"):
            return
        elif(getInp == "change-name"):
            ChangeName()
        elif(getInp == "change-lastname"):
            ChangeLastname()
        elif(getInp == "change-username"):
            ChangeUsername()
        elif(getInp == "change-password"):
            ChangePassword()
        
        AccountSettings()
    
    # Her hansi accountu silmek 
    def DeleteAccount():
        userName = input("\n- Enter username of account to delete: ")
        while( not isDeleteAccount(userName, argUsername)):
            userName = input("- Enter username of account to delete: ")
        dataList = GetDataFromJson("database.json")
        index = GetIndex(userName)
        dataList.pop(index)
        SetDataToJson("database.json", dataList)

        print("Account successfully deleted from system.\n\n")

        




    # entry point
    def AccountPage():
        
         # Selahiyyetlerin dogru olub-olmadidigini gosterir
        def isValidInput():
            userInp = input()
            if(userInp == "logout" or userInp == "show" or userInp == "delete-accs" or
               userInp == "show-accs" or userInp == "acc-settings"):
                return userInp
            else:
                print("Attention: You don't have this ability, please try againt \n")
                isValidInput()
        
        print("Your Abilities are:")
        print("- log out (logout)")
        print("- Show your data (show)")
        print("- Show all accounts data (show-accs)")
        print("- Account settings (acc-settings)")
        print("- Delete accounts (delete-accs)")
        getInp = isValidInput()

        if(getInp == "logout"):
            print("Log outing from account...")
            return
        else:
            if(getInp == "show"):
                ShowYourDatas()
            else:
                if(getInp == "show-accs"):
                    ShowAccountsData()
                else:
                    if(getInp == "acc-settings"):
                        AccountSettings()
                    else:
                        if(getInp == "delete-accs"):
                            DeleteAccount()
        AccountPage()  #recursion
                
    print(f'\n\n\nHello Welcome To Your Account! ')
    AccountPage()


# Editor Page
def CoordinatorPage(argUsername):

    # inputlarin dogru olub-olmadidigini gosterir
    def isValidInput():
        userInp = input()
        if(userInp == "logout" or userInp == "show" or
           userInp == "acc-settings"):
            return userInp
        else:
            print("Attention: You don't have this ability, please try againt \n")
            isValidInput()

    #Accountun detallarini gosterir
    def ShowYourDatas():
        print("Your datas:")
        for eachDict in GetDataFromJson("database.json"):
            for key,value in eachDict.items():
                if(key == "username" and value == argUsername):
                    for key,value in eachDict.items():
                        print(f'{key} -> {value}')     
                    print()
    
    # Accountun detallarinda deyisiklikleri gosterir
    def AccountSettings():
        # inputlarin dogru olub-olmadidigini gosterir
        def isValidInput():
            userInp = input()
            if(userInp == "back" or userInp == "change-name" or 
               userInp == "change-lastname" or userInp == "change-username" or
               userInp == "change-password"):
                return userInp
            else:
                print("Attention: You don't have this ability, please try againt \n")
                isValidInput()
        
        # Adi deyismek :
        def ChangeName(): 
            name = input("\n- Enter your new name: ")
            while(not isValidName(name)):
                name = input("- Enter your new name: ")  

            dataList = GetDataFromJson("database.json")    
            for eachDict in dataList:
                for key, value in eachDict.items():
                    if(key == "username" and value == argUsername):
                        eachDict["name"] = name
            SetDataToJson("database.json", dataList)
            print("\n-Name successfully changed!\n\n")          

        # Soyadi deyismek :
        def ChangeLastname():
            lastName = input("\n-- Enter your new last name: ")
            while(not isValidLastName(lastName)):
                lastName = input("- Enter your new last name: ")

            dataList = GetDataFromJson("database.json")    
            for eachDict in dataList:
                for key, value in eachDict.items():
                    if(key == "username" and value == argUsername):
                        eachDict["lastName"] = lastName
            SetDataToJson("database.json", dataList)
            print("\n-Last name successfully changed!\n\n")

        # Username-i deyismek :
        def ChangeUsername(): 
            userName = input("- Enter your new username: ")
            while(not isValidUsername(userName)):
                userName = input("- Enter your new username: ")

            dataList = GetDataFromJson("database.json")    
            for eachDict in dataList:
                for key, value in eachDict.items():
                    if(key == "username" and value == argUsername):
                        eachDict["username"] = userName
            SetDataToJson("database.json", dataList)
            print("\n-Username successfully changed! (Restart program to apply changes)\n\n") 

        #Sifreni deyismek
        def ChangePassword():
            print("\n-Tip: Password should contain: letters(upper, lower), symbols and numbers.")
            password = input("- Enter your new password: ")
            while(not isValidPassword(password)):
                password = input("- Enter your new password: ")

            # Confirm Password
            confirmPassword = input("- Confirm your new password: ")
            while(not isValidConfirmPassword(password, confirmPassword)):
                confirmPassword = input("- Confirm your new password: ")

            dataList = GetDataFromJson("database.json")    
            for eachDict in dataList:
                for key, value in eachDict.items():
                    if(key == "username" and value == argUsername):
                            eachDict["password"] = password
            SetDataToJson("database.json", dataList)
            print("Password successfully changed!")
            

            
        print("\n\n")
        print("You are in account settings, you can do:")
        print("- Go back to profile page (back)")
        print("- Change your name (change-name)")
        print("- Change your last name (change-lastname)")
        print("- Change your username (change-username)")
        print("- Change your password (change-password)")

        getInp = isValidInput()

        if(getInp == "back"):
            return
        elif(getInp == "change-name"):
            ChangeName()
        elif(getInp == "change-lastname"):
            ChangeLastname()
        elif(getInp == "change-username"):
            ChangeUsername()
        elif(getInp == "change-password"):
            ChangePassword()
        
        AccountSettings()


    def AccountPage():
        print("Your Abilities are:")
        print("- log out (logout)")
        print("- Show your data (show)")
        print("- Account Settings (acc-settings)")
        getInp = isValidInput()

        if(getInp == "logout"):
            print("Log outing from account...")
            return
        else:
            if(getInp == "show"):
                ShowYourDatas()
            else:
                if(getInp == "acc-settings"):
                    AccountSettings()
        AccountPage()


    print(f'\n\n\nHello, Welcome To Your Account! ')
    AccountPage()