from pathlib import Path
import os

def readFileAndFolder():
    path = Path('') # current main directory
    
    # items = list(path.rglob('*')) # rglob is used to get all the items in the current directory and subdirectories
    items = list(path.glob('*')) # glob is used to get all the items in the current directory
    
    for i, item in enumerate(items):
        print(f" {i+1} : {item} ")

def createFile():
    try: 
        readFileAndFolder()
        name = input("Please tell your filename :")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in this file : ")
                fs.write(data)

            print(F"FILE CREATED SUCCESSFULLY.")
        else:
            print("This file is already exists.")
        
    except Exception as err:
        print(f"Error occurred as {err}")
        
    
def readFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to read : ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("File data read successfully.")
        else:
            print("File does not exists.")
    except Exception as err:
        print(f"Error occurred as {err}")

def updateFile():
    try:
        readFileAndFolder()
        name = input("which file you want to update :")
        p = Path(name)

        if p.exists() and p.is_file():
            print("Press 1 for changing the name : ")
            print("Press 2 for overwriting the data into the file : ")
            print("Press 3 for appending some content in your file : ")

            res = int(input("Tell your response : "))

            if res == 1:
                name2 = input("Tell your new file name : ")
                p2 = Path(name2)
                p.rename(p2)
            
            if res == 2:
                with open(p, 'w') as fs:
                    data = input("Tell what you want to write this is overwrite the data : ")
                    fs.write(data)
                
            if res == 3:
                with open(p, 'a') as fs:
                    data = input("Tell what you want to append the data : ")
                    fs.write(" " + data)
    except Exception as err:
        print(f"Error occurred as {err}")


def deleteFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to delete : ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)

            print("File deleted successfully.")
        else:
            print("No such file exists")
    except Exception as err:
        print(f"Error occurred as {err}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file\n")

choice = int(input("Enter your choice : "))

if choice == 1:
    createFile()

if choice == 2:
    readFile()

if choice == 3:
    updateFile()

if choice == 4:
    deleteFile()