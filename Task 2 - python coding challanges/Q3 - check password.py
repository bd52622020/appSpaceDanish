#!/usr/bin/env python

def checkpass():
    pwd = True
    password = input("Please enter a password: ")
    if not re.search("[a-z]", password): 
        print('Password should have at least one lowercase letter') 
        pwd = False
    if not re.search("[A-Z]", password):  
        print('Password should have at least one uppercase letter') 
        pwd = False
    if not re.search("[@$£#%]", password):  
        print('Password should have at least one of the symbol @$£#%') 
        pwd = False
    if not re.search("[0-9]", password):   
        print('Password should have at least one numeral') 
        pwd = False
    if len(password) < 6:
        print('Password should be atleast 6 characters')
        pwd = False 
    if len(password) > 16:
        print('Password should not be longer then 16 characters')
        pwd = False 
    if pwd == True:
        print("Password is Correct")

if __name__ == "__main__":
    checkpass()
