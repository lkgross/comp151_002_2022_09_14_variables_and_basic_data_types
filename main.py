# Let's experiment with variables and data types.

# This is a string.

"Hello world"

# We can print it.
print("Hello world")

print('Hello world')

# This is an integer.

2

# We can print it.
print(2)

# This is a floating-point number.
print(17.0)

# When you do arithmetic with a floating-point number,
# the result is a floating-point number.

print(2 + 17.0)

print(2/3)

# The integer divide (//) drops the decimal part of the quotient.
print(2 // 3)

# The remainder or modulus or mod operator (%) returns the remainder.
print(17 % 2)

# The ** is for exponentiation or powers.
print(3**2)

print(2**3)

print(14_000_000)

# Remember the PEDMAS order of operations.

print(2*3 + 3*3)

print(2 * (3+3) * 3)

msg = "Hello world!"

print(msg)

msg2 = "What's your name?"

print(msg2)

class_grade = 4.0

class_credits = 3

print(class_credits)

quality_points = class_grade * class_credits

print(quality_points)

fname = "laura"

lname = "gross"

print(fname)

# We can assign more than one variable at once!
first_name, last_name = "laura", "gross"

print(first_name)

print(type(msg))

print(type(class_grade))

print(type(class_credits))

# Use all-caps for constants that you never want to change!
NATION_NAME = "USA"