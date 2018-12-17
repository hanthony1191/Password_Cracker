#Part 1: Program 1

import hashlib

def main():
    print("Welcome to Part 1")
    print("Sign Up Below\n")

    signup()

    print("Log in\n")

    username = input("Username: ")
    password = input("Password: ")

    if check(username, password):
        print("authentication successful")
    else:
        print("failed to log in")

def signup():
    pass_file = open("login.txt", "a")

    username = input("Username: ")
    password = input("Password: ")

    if not check(username, password):
        pass_file.write(username + ' ')
        
        hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
        pass_file.write(hashed_password + '\n')

        print("successfully registered")
    else:
        print("username or password already exists")

    pass_file.close()

#Part 2: Program 2

def check(username, password):
    database = open("login.txt", "r")
    records = database.readlines()

    hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
    found = False

    for user in records:
        login = user.split()
        if username == login[0] and hashed_password == login[1]:
            found = True

    return found
        
main()
