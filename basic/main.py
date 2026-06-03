print("Nastey Python...")


#comments 

"""Hello this is doc string (Comment)"""

#variables
test = "Nastey Python"

print(type(test))

#Number
a = 35.6
b = 15/3
c  = 21j

print(type(a))
print(type(b))
print(type(c))

#String
steTest = "1234TestStringJKLJ"
print(type(steTest))

#Boolean
boolTest = True
print(type(boolTest))

uniCode = "A"
print(ord(uniCode)) #ord() function returns the Unicode code point for a given character.

a = 65
print(chr(a)) #chr() function returns the character that represents the specified Unicode code point.

stringTest = "Swapnil Menkar"
print(stringTest[0:7:1]) # string slicing [start:stop:step] 0 to 6 index print and step is 1 means print every character.

print(stringTest[8::1]) # string slicing [start:stop:step] 8 to end index print and step is 1 means print every character.

print(stringTest[::]) # string slicing [start:stop:step] start to end index print and step is 1 means print every character.

# Type conversion functions - str(), int(), float(), bool()

a = 11
A = str(a)
print(type(A))
print(A)


# b = "string"
# B = int(b) # This will raise a ValueError because "string" cannot be converted to an integer.
# print(B)

# Implicit type conversion
x = 12
print(x/3) # This will result in a float (4.0) due to implicit type conversion.

name = "Swapnil"
age = 25

print(name, age) # Explicit type conversion of age to string for concatenation.

print(f"My name is {name} and I am {age} years old.") # Using f-string for formatted output.

que = input("What is your name? ") # Taking user input and storing it in the variable 'que'.
print(f"Hello, {que}!") # Greeting the user with their input name.