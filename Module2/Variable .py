# PYTHON VARIABLES
# A variable in Python is a named reference or identifier that stores a value.
# It acts as a container to hold data during program execution.
# When you use the assignment operator "=", you can assign a value to them to create them.

a = 1;
b = 2;
c = 3;
d = 4;
# e = Null;
print(e);

# print(d); print(a); print(b); print(c); print(d);


# Python interpreter allocates memory based on the values data type of variable, different data types like integers, decimals, characters, etc., can be stored in these variables.

# WHAT ARE VALUES ?
# Before learning about variables, you must know about values.

# A value is one of the essential parts of a program, like a letter or a number.

# Examples of such values can be:

# Value	        Data-Type
# 5, 9	         integers
# Hello, Ok	    string (a combination of letters)

# PYTHON VARIABLE DECLARATION

# In Python, like many other programming languages, there is no requirement to declare variables in advance explicitly.
# As soon as a value is assigned to a variable, it is automatically declared at that moment.
# This characteristic is why Python is known as a dynamically typed language.

# The syntax for creating variables in Python is given below:

# SYNTAX:

# <variable_name> = <value>

# ASSIGNING VALUES TO VARIABLES

# Python interpreter can determine what type of data is stored, so variables do not need to be declared before assigning a value.
# Usually, in all programming languages, the equal sign "=" is used to assign values to a variable.
# It assigns the values of the right-side operand to the left-side operand.
# The left side operand of the "=" operator is the name of a variable, and the right side operand is value.

# Example:
# name = "Packing box" # A string
# height = 10 # An integer assignment
# width = 20.5 # A floating point

# print (name)
# print (height)
# print (width)

# In the above code snippet, the variable name "height" is storing a value "10", and since the value is of a type integer, the variable is automatically assigned the type integer.
# Another variable name "width" is assigned with a floating type value. Then both the values are printed or displayed using the 'print' statement.

# COMMON RULES FOR NAMING VARIABLES IN PYTHON
# There are specific rules and conventions regarding variables in Python that must be followed in order to use variables correctly:

# 1)Variable Naming: Variables must follow specific naming conventions. They must begin with letters, numbers, or underscores, followed by other characters. Reserved words should not be used as variable names.
# 2)Case Sensitivity: Variables with different capitalizations are regarded as separate because Python is case-sensitive. For instance, "count" and "Count" are handled differently.
# 3)Avoid Built-in Function Names: It is advised to avoid using the names of built-in functions or modules as variable names to prevent conflicts and confusion.
# 4)Meaningful and Descriptive Names: Use informative names that reflect the variable's purpose or nature. This improves code readability and maintainability.
# 5)Snake Case Convention: Use underscores and lowercase letters to separate words in variable names, adhering to the snake_case convention. For example, "user_name" or "total_count".
# 6)Constants: Constant names typically consist of uppercase letters and underscores. For example, "PI" or "MAX_VALUE".


# PYTHON VARIABLE DELETION

# Python also provides a facility to delete a variable from memory.
# The del command is used for this. The following is the general syntax for deleting a variable in Python:

# Syntax:
# del <variable-name>
myname = "AnonymouX the hacker";
print(myname);
