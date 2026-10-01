
#An application that should check a list of broken users.

BLOCKED_USERS = ["admin", "root", "administrator"] # Creates a list of blocked users

def check_user(): #Creates a function for checking users using a colon so this is a conditional

    username = input("Enter your username: ").strip().lower() #Next statement after the condition but something is off

    if username in BLOCKED_USERS: #another conditional but two things seem off about it.

        print("Access Denied.") #Gives feedback that access is denied.

    else: #this gives us our other condition

        print("Welcome", username) #Welcomes the user if they are not one of the blocked users

check_user() #runs our function check_user

