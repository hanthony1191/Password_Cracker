#Part 3

def main():
    password = input("Input Password: ")

    passEval(password)

def passEval(password):
    weak = False
    moderate = False
    strong = False
    
    dictionary = open("dictionary.txt", "r")
    entries = dictionary.readlines()
    
    for entry in entries:
        if entry.strip() == password:
            weak = True
            break
        elif entry.strip() in password:
            moderate = True
        elif entry.strip() not in password:
            strong = True

    if weak == True:
        print("Weak Password")
    elif moderate == True:
        print("Moderate Password")
    elif strong == True:
        print("Strong Password")

    dictionary.close()

main()
