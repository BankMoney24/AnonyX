# CONCEPTS OF INDENTATION IN PYTHON 
# Indentation in Python refers to the (spaces and tabs) that are used at the beginning of a statement.
# The statements with the same indentation belong to the same group called a suite.

# Consider the example of a correctly indented Python code statement mentioned below.
# Example:

a = 1
b = 2

if a == 1:
    print(a)
    if b == 2:
        print(b)
print('end') 

# In the above code, the first and last line of the statement is related to the same suite because there is no indentation in front of them.
# So after executing the first "if statement", the Python interpreter will go into the following statement.
# If the condition is not true, it will execute the last line of the statement.

# NB:By default, Python uses four spaces for indentation, which is flexible and can be managed by the programmer.

# At the next level, the following statements are typed with four spaces(a tab) in front of them so they are in the same suite.

# Example:
    print(a)
    if b == 2:
    
#  The third statement: "if b == 2" will be executed if the first statement: "if a == 1" is true.

# In the following statement, eight spaces (two tabs) have been typed in front of "print (b)", and hence it is in a separate suite, 
# and it will execute only if the statement "if b == 2" is true.

# Example:
        print(b)