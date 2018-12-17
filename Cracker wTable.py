#Part 2
import hashlib

def main():
    #passwords = open("file.txt", "r")
    #hashed_pass = passwords.readline()
    
    password = input("Input Password: ")
    hashed_pass = hashlib.md5(password.encode('utf-8')).hexdigest()

    passSearch(hashed_pass)
    print('Finished')

def passSearch(hashed_pass):
    table = open('rainbow.txt', 'r')
    row = table.readlines()

    for data in row:
        dat = data.split()
        if hashed_pass == dat[1]:
            print(dat[0] + ": " + dat[1])
        else:
            print("Password could not be cracked")

main()
