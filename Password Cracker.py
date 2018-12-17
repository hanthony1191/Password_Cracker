#Part 2
import hashlib
import time

def main():
    start = time.time()

    #passwords = open("file.txt", "r")
    #hashed_pass = passwords.readline()
    
    password = input("Input Password: ")
    hashed_pass = hashlib.md5(password.encode('utf-8')).hexdigest()

    passCracker(hashed_pass)
    print('Finished')
    print('Time(sec): %s' %(time.time() - start))

def passCracker(hashed_pass):
    found = False
    
    dictionary = open("dictionary.txt", "r")
    entries = dictionary.readlines()

    chars = list(range(10)) + ['!', '@', '#', '$', '%']

    for entry in entries:
        hashed_entry = hashlib.md5(entry.strip().encode('utf-8')).hexdigest()

        if hashed_entry == hashed_pass:
            print(entry + " = " + hashed_entry)
            found = True
            break

    if not found:                                
        for entry in entries:
            if found:
                break
            else:
                for char in chars:
                    if found:
                        break
                    else:
                        type2 = entry.strip() + str(char)
                        type2_entry = hashlib.md5(type2.encode('utf-8')).hexdigest()

                        if type2_entry == hashed_pass:
                            print(type2 + " = " + type2_entry)
                            found = True
                            break
                        else:
                            for char in chars:
                                if found:
                                    break
                                else:
                                    type3 = type2 + str(char)
                                    type3_entry = hashlib.md5(type3.encode('utf-8')).hexdigest()

                                    if type3_entry == hashed_pass:
                                        print(type3 + " = " + type3_entry)
                                        found = True
                                        break
                                    else:
                                        for char in chars:
                                            type4 = type3 + str(char)
                                            type4_entry = hashlib.md5(type4.encode('utf-8')).hexdigest()

                                            if type4_entry == hashed_pass:
                                                print(type4 + " = " + type4_entry)
                                                found = True
                                                break
    if not found:                                
        for entry in entries:
            if found:
                break
            else:
                for char in chars:
                    if found:
                        break
                    else:
                        type2 = str(char) + entry.strip()
                        type2_entry = hashlib.md5(type2.encode('utf-8')).hexdigest()

                        if type2_entry == hashed_pass:
                            print(type2 + " = " + type2_entry)
                            found = True
                            break
                        else:
                            for char in chars:
                                if found:
                                    break
                                else:
                                    type3 = str(char) + type2
                                    type3_entry = hashlib.md5(type3.encode('utf-8')).hexdigest()

                                    if type3_entry == hashed_pass:
                                        print(type3 + " = " + type3_entry)
                                        found = True
                                        break
                                    else:
                                        for char in chars:
                                            type4 = str(char) + type3
                                            type4_entry = hashlib.md5(type4.encode('utf-8')).hexdigest()

                                            if type4_entry == hashed_pass:
                                                print(type4 + " = " + type4_entry)
                                                found = True
                                                break
    if not found:
        for entry in entries:
            if found:
                break
            else:
                for char in chars:
                    if found:
                        break
                    else:
                        type2 = str(char) + entry.strip()
                        type2_entry = hashlib.md5(type2.encode('utf-8')).hexdigest()

                        for char in chars:
                            if found:
                                break
                            else:
                                type3 = type2 + str(char)
                                type3_entry = hashlib.md5(type3.encode('utf-8')).hexdigest()

                                if type3_entry == hashed_pass:
                                    print(type3 + " = " + type3_entry)
                                    found = True
                                    break
                                else:
                                    for char in chars:
                                        type4 = type3 + str(char)
                                        type4_entry = hashlib.md5(type4.encode('utf-8')).hexdigest()

                                        if type4_entry == hashed_pass:
                                            print(type4 + " = " + type4_entry)
                                            found = True
                                            break
                                
    if not found:
        for entry in entries:
            if found:
                break
            else:
                for char in chars:
                    if found:
                        break
                    else:
                        type2 = str(char) + entry.strip()
                        type2_entry = hashlib.md5(type2.encode('utf-8')).hexdigest()

                        for char in chars:
                            if found:
                                break
                            else:
                                type3 = str(char) + type2
                                type3_entry = hashlib.md5(type3.encode('utf-8')).hexdigest()

                                for char in chars:
                                    type4 = type3 + str(char)
                                    type4_entry = hashlib.md5(type4.encode('utf-8')).hexdigest()

                                    if type4_entry == hashed_pass:
                                        print(type4 + " = " + type4_entry)
                                        found = True
                                        break

    if not found:
        print("Password could not be cracked")
    
main()
