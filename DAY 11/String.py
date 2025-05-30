# STRINGS IN PYTHON


'''

A string is a sequence of characters enclosed within single quotes (' ') or double quotes (" ").
In Python, strings are immutable, which means that once a string is created, it cannot be modified.
Strings can be created using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

'''


# Example:



#  Single quotes

x = 'Hello, World!'
print(x)
print(type(x))

# Output:

# Hello, World!
# <class 'str'>

# In the above example, we have created a string variable x using single quotes.





# Double quotes

y = "Hello, World!"
print(y)
print(type(y))

# Output:

# Hello, World!
# <class 'str'>

# In the above example, we have created a string variable y using double quotes.






# Triple quotes

z = '''Hello, World!'''
print(z)
print(type(z))

# Output:

# Hello, World!
# <class 'str'>

# In the above example, we have created a string variable z using triple quotes.






# ACCESSING CHARACTERS IN A STRING
# Characters in a string can be accessed using the index of the character.

# Example:

s = 'Hello, World!'
print(s[0])
print(s[7])

# Output:

# H
# W

# In the above example, we have accessed the first character of the string s using the index 0 
# and the eighth character using the index 7.




for character in s:
    print(character)

# Output:

# H
# e
# l
# l
# o
# ,
#
# W
# o
# r
# l
# d
# !









# Strings can be concatenated using the + operator.

# Example:

a = 'Hello'
b = 'World'
c = a + b
print(c)

# Output:

# HelloWorld

# In the above example, we have concatenated the strings a and b using the + operator.




# Strings can be repeated using the * operator.

# Example:

d = 'Hello'
e = d * 3
print(e)

# Output:

# HelloHelloHello

# In the above example, we have repeated the string d three times using the * operator.


