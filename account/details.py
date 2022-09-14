#slowprint (makes terminal print slowly)
import sys
import time
from unicodedata import name
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./25) #change the denominators value to change type speed

#define special characters
specialChar = ['!', '@', '#', '£', '¤', '$', '%', '&', '/', '{', '}', '(', ')', '[', ']', '=', '?', '+', '-', '.', '*', '^', '¨', '~', '<', '>', '|']

#validate the username
def validateUsername(name):
    
    #declare how many characters the username must contain
    if len(name) < 5 or len(name) > 15:
        slowprint("Username must contain between 5-15 characters")
        return False
    
    #declare if username should contain white spaces
    elif any(char.isspace() for char in name):
        slowprint("Username can not contain white spaces")
        return False
    
    #declare if username should contain special characters
    elif any(char in specialChar for char in name):
        slowprint("Password can not contain special characters or symbols")
        return False
        
    #if all requirements are met, username = valid
    else:
        return True

#validate the password
def validatePasswd(passwd):
    
    #declare how many characters the password must contain
    if len(passwd) < 8 or len(passwd) > 16:
        slowprint("Password must contain between 8-16 characters")
        return False
        
    #declare if password should contain upper case letters
    elif not any(char.isupper() for char in passwd):
        slowprint("Password must contain at least one upper case letter")
        return False
    
    #declare if password should contain lower case letters
    elif not any(char.islower() for char in passwd):
        slowprint("Password must contain at least one lower case letter")
        return False
    
    #declare if password should contain numbers
    elif not any(char.isdigit() for char in passwd):
        slowprint("Password must contain at least one numeral")
        return False
    
    #declare if password should contain letters
    elif not any(char.isalpha() for char in passwd):
        slowprint("Password must contain at least one letter")
        return False
    
    #declare if password should contain special characters
    elif not any(char in specialChar for char in passwd):
        slowprint("Password must contain at least one special character")
        return False
    
    #declare if password should contain white spaces
    elif any(char.isspace() for char in passwd):
        slowprint("Password can not contain white spaces")
        return False
    
    #if all requirements are met, password = valid
    else: 
        return True

#program intro
slowprint("Hi, creating an account is easy and free! Just follow the steps down below")

#ask for new username
name=input("Insert your new username: ")

#if username validation is declined, try again
while validateUsername(name) == False:
    name=input("Insert your new username: ")
    
#validation information
if validateUsername(name) == True:
    slowprint("Username valid!")

#ask for new password
passwd=input("Insert your new password: ")

#if password validation is declined, try again
while validatePasswd(passwd) == False:
    passwd=input("Insert your new password :")

#validation information
if validatePasswd(passwd) == True:
    slowprint("Password valid!")
    
    
file = open("account/user.txt", "w")
file.write("username = " + repr(name) + " " + "password = " + repr(passwd) + "\n")

file.close()

print("Welcome "+ name+ "!")