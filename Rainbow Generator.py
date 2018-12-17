#Part 2
import hashlib

def main():
    passTable()

def passTable():
    dictionary = open("dictionary.txt", "r")
    entries = dictionary.readlines()

    chars = list(range(10)) + ['!', '@', '#', '$', '%']

    for entry in entries:
        rainbow = []
        
        hashed_entry = hashlib.md5(entry.strip().encode('utf-8')).hexdigest()

        rainbow.append(entry + " " + hashed_entry)
        writeTable(rainbow)

        for char in chars:
            rainbow = []
            type2 = entry + str(char)
            type2_entry = hashlib.md5(type2.encode('utf-8')).hexdigest()

            rainbow.append(type2 + " " + type2_entry)
            writeTable(rainbow)
            
            for char in chars:
                rainbow = []
                
                type3 = type2 + str(char)
                type3_entry = hashlib.md5(type3.encode('utf-8')).hexdigest()

                rainbow.append(type3 + " " + type3_entry)
                writeTable(rainbow)
                
                for char in chars:
                    rainbow = []
                    
                    type4 = type3 + str(char)
                    type4_entry = hashlib.md5(type4.encode('utf-8')).hexdigest()

                    rainbow.append(type4 + " " + type4_entry)
                    writeTable(rainbow)
                                
    for entry in entries:
        for char in chars:
            rainbow = []
            
            type2 = str(char) + entry.strip()
            type2_entry = hashlib.md5(type2.encode('utf-8')).hexdigest()

            rainbow.append(type2 + " " + type2_entry)
            writeTable(rainbow)
            
            for char in chars:
                rainbow = []
                    
                type3 = str(char) + type2
                type3_entry = hashlib.md5(type3.encode('utf-8')).hexdigest()

                rainbow.append(type3 + " " + type3_entry)
                writeTable(rainbow)
                
                for char in chars:
                    rainbow= []
                
                    type4 = str(char) + type3
                    type4_entry = hashlib.md5(type4.encode('utf-8')).hexdigest()

                    rainbow.append(type4 + " " + type4_entry)
                    writeTable(rainbow)
                            
    for entry in entries:
        for char in chars:
            type2 = str(char) + entry.strip()

            for char in chars:
                rainbow = []
                
                type3 = type2 + str(char)
                type3_entry = hashlib.md5(type3.encode('utf-8')).hexdigest()

                rainbow.append(type3 + " " + type3_entry)
                writeTable(rainbow)
                
                for char in chars:
                    rainbow = []
                
                    type4 = type3 + str(char)
                    type4_entry = hashlib.md5(type4.encode('utf-8')).hexdigest()

                    rainbow.append(type4 + " " + type4_entry)
                    writeTable(rainbow)
                                
    for entry in entries:
        for char in chars:
            type2 = str(char) + entry.strip()

            for char in chars:
                type3 = str(char) + type2

                for char in chars:
                    rainbow = []
                
                    type4 = type3 + str(char)
                    type4_entry = hashlib.md5(type4.encode('utf-8')).hexdigest()

                    rainbow.append(type4 + " " + type4_entry)
                    writeTable(rainbow)

    dictionary.close()
    return rainbow

def writeTable(rainbow):
    table = open('rainbow.txt', 'a')
    
    for combo in rainbow:
        table.write("%s\n" % combo)

    table.close()
    
main()
