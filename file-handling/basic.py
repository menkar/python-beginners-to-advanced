# file = open(r"README.md")

# print(file.read())

file = open("./file-handling/Test.txt", 'w')
file.write("Hello, I am Swapnil. I am writing in this file. Added some more details....")

file.close()

fileRead = open("./file-handling/Test.txt", "r")
print(fileRead.read())


fileRead = open("./file-handling/Test.txt", "a")
fileRead.write("Appending some more detailed infomration here....")

fileRead.close()

fileRead = open("./file-handling/Test.txt", "r")
print(fileRead.read())

fileRead = open("./file-handling/Test-Create.txt", "x")
fileRead.close()

fileRead = open("./file-handling/Test-Create.txt", "r")
print(fileRead.read())

