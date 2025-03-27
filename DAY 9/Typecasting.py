# TYPECASTING IN PYTHON 

'''

Typecasting is the process of converting the data type of a variable to another data type.
In Python, we can convert the data type of a variable to another data type using the following functions:

'''





# int() - converts a variable to an integer
# float() - converts a variable to a float
# str() - converts a variable to a string
# bool() - converts a variable to a boolean

# Example:

x = 10
y = float(x)
print(y)
print(type(y))

# Output:

# 10.0
# <class 'float'>

# In the above example, we have converted the integer variable x to a float variable y using the float()





# There are two types of typecasting in python:



# 1. Implicit Typecasting
# 2. Explicit Typecasting



# 1. Implicit Typecasting

# Implicit typecasting is the automatic conversion of a variable from one data type to another data type.

# Example:

a = 10
b = 5.5
c = a + b
print(c)
print(type(c))

# Output:

# 15.5
# <class 'float'>

# In the above example, the integer variable a is implicitly converted to a float variable b during the addition operation.







# 2. Explicit Typecasting

# Explicit typecasting is the manual conversion of a variable from one data type to another data type.

# Example:

a = 10
b = 5.5
c = a + int(b)
print(c)
print(type(c))

# Output:

# 15
# <class 'int'>

# In the above example, the float variable b is explicitly converted to an integer variable using the int() function.
