from register import Register
from login import Login


while (True):
    print("""
What do you want to do?
- Log in to account (type: login)
- Register new account (type: reg)
- Exit from program (type: exit)
    """)

    getInput = input()
    print()
    
    if(getInput == "login"):
        Login()
    
    if(getInput == "reg"):
        Register()

    if(getInput == "exit"):
        print("Program terminates....")
        break

    
    









