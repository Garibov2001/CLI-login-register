import json
from databaseConfig import *

# Gonderilen string herflerden teskil olub ya yox:
def isAlpha(argText):
    for i in range(0,len(argText)):
        if(argText[i].lower() == argText[i] and
           argText[i].upper() == argText[i]):
           return False
    return True
 

#Gonderilen stringin yalniz ilk ilk herifi boyukdurmu
def isCapitalized(argText):
    if(argText[0].lower() != argText[0] and
       argText[0].upper() == argText[0]):
        for i in range(1, len(argText)):
            if(argText[i].lower() == argText[i] and
               argText[i].upper() != argText[i]):
               continue
            else:
                return False
        return True
    else:
        return False


# Gonderilen stringin bosdurmu
def isEmpty(argText):
    if (len(argText) == 0):
        return True
    else:
        return


#Gonder string daxilinde Space varmi
def isSpace(argText):
    for i in range(len(argText)):
        if(argText[i] == " "):
            return True
    return False


#Adin dogrulugunu yoxlayir:
def isValidName(argText):
    if(not isEmpty(argText)):
        if(not isSpace(argText)):
            if(isAlpha(argText)):                
                if(isCapitalized(argText)):
                    return True
                else:
                    print("Attention: Only first letter can be uppercase.\n")
                    return False
            else:
                print("Attention: Name can contain only letters.\n")
                return False     
        else:
            print("Attention: Name can't contain space.\n")
            return False
    else:
        print("Attention: Please fill the name area.\n")
        return False


#Soyadin dogrulugunu yoxlayir:
def isValidLastName(argText):
    if(not isEmpty(argText)):
        if(not isSpace(argText)):
            if(isAlpha(argText)):
                if(isCapitalized(argText)):
                    return True
                else:
                    print("Attention: Only first letter can be Uppercase.\n")
                    return False
            else:
                print("Attention: Last name can contain only letters.\n")
                return False  
        else:
            print("Attention: Last name can't contain space.\n")
            return False   
    else:
        print("Attention: Please fill the last name area.\n")
        return False


# Username sistemde varmi (register ucun):
def isUsernameExist(argText, isEnter = False):
    for eachDict in GetDataFromJson("database.json"):
        for key, value in eachDict.items():
            if(key == "username" and value == argText):
                return True
    if(isEnter):
        print("Attention: This username doesn't exist in system.\n")
    return False      


# Daxil edilen username dogrudurmu
def isValidUsername(argText):
    if(not isEmpty(argText)):
        if(not isSpace(argText)):
            if(not isUsernameExist(argText)):
                return True
            else:
                print("Attention: This username is already exist.\n")  
        else:
            print("Attention: Username can't contain space.\n")
            return False          
    else:
        print("Attention: Please fill the username area..\n")
        return False


# Daxil edilen sifre sistemde varmi (wrong/true) 
def isPasswordTrue(argPassword, argUsername):
    for eachDict in GetDataFromJson("database.json"):
        for key,value in eachDict.items():
            if(key == "username" and value == argUsername):
                for key,value in eachDict.items():
                    if(key == "password" and value == argPassword):
                        return True                    
                print("Attention: Password is wrong!")
                return False


# Daxil edilen sifre standartlara uyurmu 
def isValidPassword(argText):
    if(not isEmpty(argText)): 
        if(not isSpace(argText)):       
            if(isLowerExist(argText)):            
                if(isUpperExist(argText)):                       
                    if(isSymbolExist(argText)): 
                        if(isDigitExist(argText)): 
                            return True
                        else:
                            print("Attention: password has to contain number.\n")
                            return False                      
                    else:
                        print("Attention: password has to contain symbol.\n")
                        return False                     
                else:
                    print("Attention: password has to contain uppercase letter.\n")
                    return False
            else:
                print("Attention: password has to contain lowecase letter.\n")
                return False
        else:
            print("Attention: Password can't contain space.\n")
            return False
    else:
        print("Attention: Please fill the password area.\n")
        return False


# Daxile edilien sifreni confirm et
def isValidConfirmPassword(firstPass, secondPass):
        if(firstPass == secondPass):
            return True
        print("Passwords doesn't match")
        return False


# Gonderilen stringde en azi birdene kicik herf varmi
def isLowerExist(argText):
    for i in range(0,len(argText)):
        if(argText[i].lower() == argText[i] and
            argText[i].upper() != argText[i]):
            return True
    return False


# Gonderilen stringde en azi birdene boyuk herf varmi
def isUpperExist(argText):
    for i in range(0,len(argText)):
        if(argText[i].lower() != argText[i] and
            argText[i].upper() == argText[i]):
            return True
    return False


# Gonderilen stringde en azi birdene simvol varmi
def isSymbolExist(argText):
    for i in range(0,len(argText)):
        if(argText[i].lower() == argText[i] and
           argText[i].upper() == argText[i] and
          not (ord(argText[i]) >= 48 and ord(argText[i]) <= 57)):
            return True
    return False


# Gonderilen stringde en azi birdene reqem varmi
def isDigitExist(argText):
    for i in range(0,len(argText)):
        if(ord(argText[i]) >= 48 and ord(argText[i]) <= 57 ):
            return True
    return False


# Gonderilen username - in aid oldugu dictin list daxilinde 
# hansi indexde yerlesdiyini mueyyen edir
def GetIndex(argUsername):
    index = 0
    for eachDict in GetDataFromJson("database.json"):
        for key, value in eachDict.items():
            if(key == "username"):
                if(value == argUsername):
                    return index 
        index += 1
    return -1


# Silinmek istenilen username standartlara uygundurmu
def isDeleteAccount(argUsername, yourUsername):
    if(not isEmpty(argUsername)):
        if(not isSpace(argUsername)):
            if (argUsername != yourUsername):
                if(isUsernameExist(argUsername)):
                    return True
                else:
                    print("Attention: This username doesn't exist.\n")  
            else:
                print("Attention: You cannot delete your account.\n")
        else:
            print("Attention: Username can't contain space.\n")
            return False          
    else:
        print("Attention: Please fill the username area..\n")
        return False

                            



