a = 20
b = 8

print(a/b)
print(a//b) # floor division operator - returns the largest integer less than or equal to the result of the division.

print(5**2) # exponentiation operator - returns the result of raising the first operand to the power of the second operand.

print("A" > "B") # Comparing ASCII values of characters. "A" has a lower ASCII value than "B", so this will return False.

#print("A" > 21); # This will raise a TypeError because you cannot compare a string ("A") with an integer (21).


print( 21 > 11 and 20 > 21 and 7 > 21 ) # This will return False because while 21 > 11 is True, the other two comparisons are False, and the 'and' operator requires all conditions to be True for the overall expression to be True.

print( 21 > 11 or 20 > 21 or 7 > 21 or 51 > 21) # This will return True because the 'or' operator requires at least one condition to be True for the overall expression to be True, and in this case, 21 > 11 is True.

print( not 21 == 21) # This will return False because 21 == 21 is True, and the 'not' operator negates it, resulting in False.