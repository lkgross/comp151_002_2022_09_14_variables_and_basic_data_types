# Let's experiment with variables and data types.

# This is a string.
"Hello from the editor!"

# We can print it.
print("Hello from the editor!")

type("Hello World")

print(type("Hello World"))

# This is an integer.
2

# This is a floating-point number.
17.0

# That when you do arithmetic with a floating-point number,
# the result is a floating-point number.

2+17.0

print(2 + 17.0)
print(type(2 + 17.0))

print(2 + 3)

# Remember the PEDMAS order of operations.
print(2*3 + 3*3)

print(2*(3 + 3)*3)

print(type(2*(3+3)*3))

# The integer divide (//) drops the decimal part of the quotient.
print(2 // 3)

print(15 // 2)

# The remainder or modulus or mod operator (%) returns the remainder.
print(17 % 2)

# The ** is for exponentiation or powers.
print(3**2)

print(2**3)

msg = "Hello World!"

print(type(msg))

print(msg)

msg2 = "What's your name?"

print(msg2)

class_grade = 4.0

print(class_grade)

class_credits = 3

print(class_credits)

quality_points = class_grade * class_credits

print(quality_points)

fname = "laura"

lname = "gross"

# We can assign more than one variable at once!
first_name, last_name = "laura", "gross"

print(first_name)

# Use all-caps for constants that you never want to change!
NATION_NAME = "USA"

