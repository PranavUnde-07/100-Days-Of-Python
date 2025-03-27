# INPUT FUNCTION

'''

 The input() function is used to take input from the user. 
 The input() function reads the input from the user as a string.
 If you want to take input as an integer, 
 you need to typecast it to an integer using the int() function.
 
 '''


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum of two numbers is: ", x+y)
print("Difference of two numbers is: ", x-y)
print("Product of two numbers is: ", x*y)
print("Division of two numbers is: ", x/y)



# OR


x = input("Enter first number: ")
y = input("Enter second number: ")

print( int(x)+int(y))
print( int(x)-int(y))
print( int(x)*int(y))
print(int(x)/int(y))

# In the above code, 
# we are taking two numbers as input from the user and performing the arithmetic operations on them.
