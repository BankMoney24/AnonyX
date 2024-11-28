PYTHON OPERATORS  
Operators are integral to Python programming because they combine values and identifiers to form expressions and statements.
They act as fundamental building blocks, enabling various operations, such as mathematical calculations, logical comparisons, assignment of values,
and more, for writing effective Python code.


OPERATORS AND OPERANDS 
Python operators are symbols that are used to perform mathematical or logical manipulations.
Operands are the values or variables with which operators are applied, and the values of operands can be manipulated using operators.

Let us take a Scenario:

6 + 2, where there are two operands, a plus is the "+" operator, and the result will be 8.

In the above text, a single operator is used to manipulate the values. 
The "+" operator performs addition, "-" performs subtraction, "*" performs multiplication, "/" performs division, and "**" performs exponentiation.


TYPES OF PYTHON OPERATORS 
Python programming language is rich with built-in operators.

Python supports the following types of operators:
Arithmetic Operators
Assignment Operators
Comparison (Relational) Operators
Logical Operators
Identity Operators
Bitwise Operators
Membership Operators

ARITHEMTIC OPERATORS 

Symbol	Operator-Name	   Description
+	    Addition	       Adds the values on either side of the operator and calculates a result.
-	    Subtraction	       Subtracts values of right-side operand from left-side operand.
*	    Multiplication	   Multiplies the values on both sides of the operator.
/	    Division	       Divides the left-side operand with the right-side operand.
%	    Modulus	           It returns the remainder by dividing the left-side operand with the right-side operand.
**	    Exponent	       Calculates the exponential power
//	    Floor Division     Here the result is the quotient in which the digits after decimal points are not considered. 


ASSIGNMENT OPERATORS 

Symbol	Operator-Name	             Description
=	    Equal	                 Assigns the values of the right-side operand to the left-side operand.
+=  	Add AND	                 Adds right-side operand value to the left-side operand value and assigns the results to the left.
-=  	Subtract AND	         Subtracts right-side operand value to the left-side operand value and assigns the results to the left operand.
*=  	Multiply AND	         Similarly, it does their respective operations and assigns the operator value to the left operand.
/=	    Division AND
%=	    Modulus AND
**=	    Exponent AND
//=	    Floor Division AND



COMPARISON (RELATIONAL) OPERATORS 

Symbol	  Operator-Name	                 Description
==	      Double Equal             	If the two values of its operands are equal, then the condition becomes true, otherwise false
!= or <>  Not Equal To	            If two operands' values are unequal, the condition becomes true. Both operators define the same meaning and function.
>	      Greater Than	            If the value of the left-hand operand is greater than that of the right-hand operand, the condition becomes true.
<	      Less Than	                If the value of the left-hand operand is less than that of the right, then the condition becomes true.
<=	      Less Than Equal To	    If the value of the left-hand operand is less than or equal to that of the right-hand operand, the condition becomes true.
>=	      Greater Than Equal To	    If the value of the left-hand operand is greater than or equal to that of the right-hand operand, the condition becomes true.


LOGICAL OPERATORS

Symbol	Operator-Name	                   Description
or	     Logical OR	                   The condition is true if any of the two operands are non-zero.
and	     Logical AND	               If both the operands are true, then the condition is true.
not    	 Logical NOT  	               It is used to reverse the logical state of its operand.

IDENTITY OPERATORS 
For comparing the memory locations of two objects, identity operators are used.

There are two types of identity operators. These are:

Symbol	Operator-Name	                  Description
is	     is	                The result becomes true if values on either side of the operator point to the same object and False otherwise.
is not   is not	            The result becomes False if the variables on either side of the operator point to the same object.

BITWISE OPERATORS 

These operators are used to manipulate bits, & perform bit-by-bit operations.

There are six types of bitwise operators supported by Python. These are:

Symbol	Operator-Name	                      Description
&	     Binary AND	                  This operator copies the bit to the result if it exists in both operands.
|	     Binary OR	                  This operator copies the bit if it exists in either of the operands.
^	     Binary XOR	                  This operator copies the bit if it is set in one operand but not both.
~	     Binary 1s Complement	      This is a unary operator and can 'flip' bits.
<<	     Binary Left Shift	          The left operand value is moved left by the number of bits specified by the right operand using this operator.
>>	     Binary Right Shift	          The left operand value is moved right by the number of bits specified by the right operand using this operator.

MEMBERSHIP OPERATORS 

Symbol	  Operator-Name	               Description
in	        in	               The result of this operation becomes True if it finds a value in a specified sequence & False otherwise.
not in	  not in	           The result of this operation becomes True if it doesn't find a value in a specified sequence and False otherwise.