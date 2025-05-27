# STRING METHODS

# In this example, we will learn about some string methods in Python.






# 1. upper() - This method converts all the characters in a string to uppercase.

# Example:

name = "harry"
print(name.upper())

# Output:

# HARRY

# In the above example, we have converted all the characters 
# in the string 'harry' to uppercase using the upper() method.







# 2. lower() - This method converts all the characters in a string to lowercase.

# Example:

name = "HARRY"
print(name.lower())

# Output:

# harry

# In the above example, we have converted all the characters 
# in the string 'HARRY' to lowercase using the lower() method.







# 3. strip() - This method removes any leading (spaces at the beginning) and 
# trailing (spaces at the end) characters (space is the default leading character to remove)

# Example:

name = "   Harry   "
print(name.strip())

# Output:

# Harry

# In the above example, we have removed the leading and trailing spaces from the string 
# '   Harry   ' using the strip() method.







# 4. replace() - This method replaces a specified substring with another substring in a string.

# Example:

name = "Harry"
print(name.replace("H", "P"))
print(name.replace("r", "s"))

# Output:

# Parry
# Hassy

# In the above example, we have replaced the character 'H' with 'P' and
# the character 'r' with 's' in the string 'Harry' using the replace() method.






# 5. split() - This method splits a string into a list of substrings based on a specified delimiter.

# Example:

name = "Harry, Ron, Hermione"
print(name.split(","))

# Output:

# ['Harry', ' Ron', ' Hermione']

# In the above example, we have split the string 'Harry, Ron, Hermione' into a list 
# of substrings based on the delimiter ',' using the split() method.





# 6. join() - This method joins the elements of an iterable (list, tuple, string, etc.)

# Example:

name = ["Harry", "Ron", "Hermione"]
print(", ".join(name))

# Output:

# Harry, Ron, Hermione

# In the above example, we have joined the elements of the list 'name' using the join() method.








# 7. capitalize() - This method converts the first character of a string to uppercase and the rest to lowercase.

# Example:

name = "harry potter"
print(name.capitalize())

# Output:

# Harry potter

# In the above example, we have converted the first character of the string 'harry potter' to uppercase
# and the rest to lowercase using the capitalize() method.







# 8. title() - This method converts the first character of each word in a string to uppercase.

# Example:

name = "harry potter"
print(name.title())

# Output:

# Harry Potter

# In the above example, we have converted the first character of each word in the string
#  'harry potter' to uppercase
# using the title() method.






# 9. count() - This method returns the number of occurrences of a substring in a string.

# Example:

name = "Harry Potter"
print(name.count("r"))
print(name.count("rr"))

# Output:

# 2
# 1

# In the above example, we have counted the number of occurrences of the substring
#  'r' and 'rr' in the string 'Harry Potter'using the count() method.






# 10. find() - This method returns the index of the first occurrence of a substring in a string.

# Example:

name = "Harry Potter"
print(name.find("r"))

# Output:

# 2

# In the above example, we have found the index of the first occurrence of
#  the substring 'r' in the string 'Harry Potter' using the find() method.






# 11. index() - This method returns the index of the first occurrence of a substring in a string.

# Example:

name = "Harry Potter"
print(name.index("r"))

# Output:

# 2

# In the above example, we have found the index of the first occurrence of
#  the substring 'r' in the string 'Harry Potter' using the index() method.







# 12. startswith() - This method returns True if a string starts with a specified prefix.

# Example:

name = "Harry Potter"
print(name.startswith("Harry"))
print(name.startswith("Potter"))

# Output:

# True
# False

# In the above example, we have checked if the string 'Harry Potter' starts with
#  the prefixes 'Harry' and 'Potter'using the startswith() method.







# 13. endswith() - This method returns True if a string ends with a specified suffix.

# Example:

name = "Harry Potter"
print(name.endswith("Potter"))
print(name.endswith("Harry"))

# Output:

# True
# False

# In the above example, we have checked if the string 'Harry Potter' ends with
#  the suffixes 'Potter' and 'Harry' using the endswith() method.








# 14. isalpha() - This method returns True if all the characters in a string are alphabetic.

# Example:

name = "Harry"
print(name.isalpha())

# Output:

# True

# In the above example, we have checked if all the characters in the string 'Harry' are alphabetic
# using the isalpha() method.







# 15. isdigit() - This method returns True if all the characters in a string are digits.

# Example:

name = "12345"
print(name.isdigit())

# Output:

# True

# In the above example, we have checked if all the characters in the string '12345' are digits








# 16. isalnum() - This method returns True if all the characters in a string are alphanumeric.

# Example:

name = "Harry123"
print(name.isalnum())

# Output:

# True

# In the above example, we have checked if all the characters in the string 'Harry123' are alphanumeric
# using the isalnum() method.







# 17. islower() - This method returns True if all the characters in a string are lowercase.

# Example:

name = "harry"
print(name.islower())

# Output:

# True

# In the above example, we have checked if all the characters in the string 'harry' are lowercase
# using the islower() method.







# 18. isupper() - This method returns True if all the characters in a string are uppercase.

# Example:

name = "HARRY"
print(name.isupper())

# Output:

# True

# In the above example, we have checked if all the characters in the string 'HARRY' are uppercase
# using the isupper() method.







# 19. isspace() - This method returns True if all the characters in a string are whitespaces.

# Example:

name = "   "
print(name.isspace())

# Output:

# True

# In the above example, we have checked if all the characters in the string '   ' are whitespaces
# using the isspace() method.







# 20. swapcase() - This method swaps the case of all the characters in a string.

# Example:

name = "Harry Potter"
print(name.swapcase())

# Output:

# hARRY pOTTER

# In the above example, we have swapped the case of all the characters in the string 'Harry Potter'
# using the swapcase() method.







# 21. center() - This method returns a centered string of a specified length.

# Example:

name = "Harry"
print(name.center(10))

# Output:

#   Harry

# In the above example, we have centered the string 'Harry' in a string of length 10
# using the center() method.
