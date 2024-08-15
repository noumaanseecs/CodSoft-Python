#TASK 2 : CALCULATOR
print('This is a simple calculator \n')
print("For Addition : + \n For Subtraction : -\n For Multiplication : *\n For Division : /\n For Modulus / Remainder : % \n")
# PROMPTS USER TO ENTER 2 DIGITS
a = float(input('Enter first number : '))
b = float(input('Enter second number : '))

# PROMPTS USER TO ENTER OPERATOR

op = input('Enter Operation to be performed: ')

# print(" For Addition : +  \n For Subtraction : - \n For Multiplication : * \n For Division : / \n For Modulus / Remainder : % ")

# HERE I USED A CONDITIONAL STRUCTURE TO DECIDE THE OPERATION TO BE PERFORMED BASED ON INPUT

# ADDITION

if op == '+':
    print(f"Sum = ",a+b)

# MULTIPLICATION

elif op == '*':
    print(f"Product = ",a*b)

# SUBTRACTION

elif op == '-':
    print(f"Difference = ",a-b)

# DIVISION

elif op == '/':
    print(f"Division = ",a/b)

# MODULUS / REMAINDER

elif op == '%':
    print(f"Modulus = ",a%b)

# DISPLAYS ERROR MESSAGE IF USER INPUTS WRONG OPERAND

else:
    print('Invalid Operand.')

