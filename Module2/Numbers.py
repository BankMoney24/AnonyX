# PYTHON NUMBERS  
# In programming, the basic building blocks for a program include variables, strings, data types, and numbers. We specifically highlight support for integers, floating-point numbers, and complex numbers when referring to numbers in Python.
# These numeric data types enable the storage and manipulation of various numerical values.
# When values are assigned to variables of this type, Number objects are created, allowing mathematical operations and computations in Python programs.

Example:
variable_name1 = 10

variable_name2 = 6.2 

# Using the "del" statement in Python makes it possible to delete references to number objects explicitly.
# The syntax for the "del" statement is as follows:
    
# Syntax:
# del variable_name

# Example:
x = 10
y = 5
z = 7

del x, y, z 

# The following data types are used to define numeric variables in Python:
# int
# float
# complex

# These data types act as classes in Python. Integers represent whole numbers without decimal points, such as 6, while floating-point values (floats) represent decimal or fractional numbers, like 6.2. 
# The complex numbers combine real and imaginary parts, denoted as a + bj.

# TYPES OF NUMERICAL DATA TYPES   

# Python provides four distinctive numerical types:

# Numerical-Type    	                       Description	                                                                   Example
# Signed Integers	        Range of positive and negative whole numbers without a decimal point.	                            x = 10
# Float (Real Values)	    Represents real numbers with a decimal point for division between the integer and fraction. 	   z = 3.14
# Complex Numbers	        Represented as "a + bJ", where "a" and "b" are floating-point numbers                             w = 2 + 3j
#                          	and "J" is the square root of -1 (imaginary number).  


# TYPE CONVERSION (CASTING)

# Python provides convenient functions for converting values between different types within an expression:

# Function	     Description	                                                                            Example          	Result
# int(v)	        Converts a value 'v' to a plain integer.	                                                int(3.5)	          3
# float(v)	    Converts a value 'v' to a floating-point value.	                                            float(3)	          3.0
# complex(v)	    Converts a value 'v' to a complex number with the real part 'v'.	                        complex(3)	        (3+0j)
# complex(u, v)	Converts 'u' and 'v' to a complex number with the real part 'u' and imaginary part 'v'.	    complex(3, 4)	     (3+4j)


# These conversion functions allow the seamless conversion of values between different numeric types in Python. 
# They can be used within expressions to ensure compatibility and perform accurate calculations.

# Example:

x = 10.5
y = 5

#without type cast
print (x + y) 

#after type cast
print (int(x) + y)

# The example above shows how to convert a float to an integer.