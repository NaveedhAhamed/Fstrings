from datetime import datetime
import math

# ==========================================================
# 1. BASIC F-STRINGS
# ==========================================================

name = "Naveedh"
age = 20
country = "Sri Lanka"

print("\n--- 1. BASIC F-STRINGS ---")
print(f"My name is {name}")
print(f"I am {age} years old.")
print(f"I live in {country}.")
print(f"My name is {name}, I am {age}, and I live in {country}.")


# ==========================================================
# 2. EXPRESSIONS INSIDE F-STRINGS
# ==========================================================

print("\n--- 2. EXPRESSIONS ---")
a = 15
b = 5

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Power: {a} ** 2 = {a ** 2}")
print(f"Square root of 25: {math.sqrt(25)}")
print(f"Uppercase name: {name.upper()}")


# ==========================================================
# 3. FORMATTING DECIMAL NUMBERS
# ==========================================================

print("\n--- 3. DECIMAL FORMATTING ---")
price = 1234.56789

print(f"Price to 2 decimal places: {price:.2f}")
print(f"Price to 3 decimal places: {price:.3f}")
print(f"Rounded to no decimal places: {price:.0f}")

percentage = 0.8567
print(f"Percentage: {percentage:.2%}")


# ==========================================================
# 4. THOUSANDS SEPARATOR
# ==========================================================

print("\n--- 4. THOUSANDS SEPARATOR ---")
population = 25_000_000
salary = 125_000.50

print(f"Population: {population:,}")
print(f"Salary: {salary:,.2f}")
print(f"Population with underscore separator: {population:_}")


# ==========================================================
# 5. WIDTH, ALIGNMENT, AND FILL CHARACTERS
# ==========================================================

print("\n--- 5. WIDTH AND ALIGNMENT ---")
word = "Python"

print(f"Default width: |{word:15}|")
print(f"Left aligned:  |{word:<15}|")
print(f"Right aligned: |{word:>15}|")
print(f"Centered:      |{word:^15}|")
print(f"Centered with * fill: |{word:*^15}|")
print(f"Right aligned with - fill: |{word:->15}|")
print(f"Left aligned with . fill: |{word:.<15}|")


# ==========================================================
# 6. SIGN FORMATTING
# ==========================================================

print("\n--- 6. SIGN FORMATTING ---")
positive = 250
negative = -150

print(f"Default positive: {positive}")
print(f"Always show sign: {positive:+}")
print(f"Negative with sign: {negative:+}")
print(f"Space reserved for positive sign: |{positive: }|")


# ==========================================================
# 7. NUMBER BASE FORMATTING
# ==========================================================

print("\n--- 7. NUMBER BASES ---")
number = 255

print(f"Decimal: {number:d}")
print(f"Binary: {number:b}")
print(f"Octal: {number:o}")
print(f"Hexadecimal: {number:x}")
print(f"Hexadecimal uppercase: {number:X}")


# ==========================================================
# 8. F-STRING DEBUGGING WITH =
# ==========================================================

print("\n--- 8. DEBUGGING WITH = ---")
x = 100
y = 50

print(f"{x=}")
print(f"{y=}")
print(f"{x + y=}")
print(f"{name.upper()=}")


# ==========================================================
# 9. STRING CONVERSIONS: !s, !r, !a
# ==========================================================

print("\n--- 9. STRING CONVERSIONS ---")
text = "Hello\nPython"

print(f"Using !s (str): {text!s}")
print(f"Using !r (repr): {text!r}")
print(f"Using !a (ascii): {text!a}")


# ==========================================================
# 10. CONDITIONAL EXPRESSIONS
# ==========================================================

print("\n--- 10. CONDITIONAL EXPRESSIONS ---")
marks = 75

result = "Pass" if marks >= 50 else "Fail"
print(f"Marks: {marks}")
print(f"Result: {result}")
print(f"Status: {'Excellent' if marks >= 75 else 'Needs improvement'}")


# ==========================================================
# 11. WORKING WITH DICTIONARIES
# ==========================================================

print("\n--- 11. DICTIONARIES ---")
student = {
    "name": "Naveedh",
    "age": 20,
    "marks": 87.5
}

print(f"Student: {student['name']}")
print(f"Age: {student['age']}")
print(f"Marks: {student['marks']:.2f}")

# Use single quotes inside the expression for compatibility
# with Python versions earlier than 3.12.
print(f"Student name: {student['name']}")


# ==========================================================
# 12. DATE AND TIME FORMATTING
# ==========================================================

print("\n--- 12. DATE AND TIME ---")
now = datetime.now()

print(f"Current date: {now:%d-%m-%Y}")
print(f"Current time: {now:%H:%M:%S}")
print(f"Day: {now:%A}")
print(f"Month: {now:%B}")
print(f"Full date: {now:%A, %d %B %Y}")


# ==========================================================
# 13. NESTED / DYNAMIC F-STRING FORMATTING
# ==========================================================

print("\n--- 13. DYNAMIC FORMATTING ---")
width = 10
precision = 2
value = 123.45678

print(f"Formatted number: {value:{width}.{precision}f}")

alignment = "^"
print(f"Dynamically centered: {name:{alignment}15}")


# ==========================================================
# 14. OBJECT FORMATTING
# ==========================================================

print("\n--- 14. OBJECT FORMATTING ---")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} scored {self.marks} marks"


student1 = Student("Naveedh", 95)

print(f"Student information: {student1}")
print(f"Student name: {student1.name}")
print(f"Student marks: {student1.marks}")


# ==========================================================
# 15. REAL-WORLD EXAMPLE: STUDENT REPORT
# ==========================================================

print("\n--- 15. STUDENT REPORT ---")
student_name = "Naveedh"
maths = 85
physics = 92
chemistry = 88

total = maths + physics + chemistry
average = total / 3

print("=" * 40)
print(f"{'STUDENT REPORT':^40}")
print("=" * 40)
print(f"Name       : {student_name}")
print(f"Mathematics: {maths:>5}")
print(f"Physics    : {physics:>5}")
print(f"Chemistry  : {chemistry:>5}")
print("-" * 40)
print(f"Total      : {total:>5}")
print(f"Average    : {average:>5.2f}")
print(f"Percentage : {average / 300:.2%}")
print("=" * 40)


# ==========================================================
# 16. REAL-WORLD EXAMPLE: SHOPPING RECEIPT
# ==========================================================

print("\n--- 16. SHOPPING RECEIPT ---")
product = "Gaming Mouse"
quantity = 2
unit_price = 4500.50

total_price = quantity * unit_price

print("=" * 40)
print(f"{'SHOPPING RECEIPT':^40}")
print("=" * 40)
print(f"Product   : {product}")
print(f"Quantity  : {quantity}")
print(f"Unit price: Rs. {unit_price:,.2f}")
print("-" * 40)
print(f"TOTAL     : Rs. {total_price:,.2f}")
print("=" * 40)


# ==========================================================
# END OF PROGRAM
# ==========================================================

print("\nAll F-String examples completed successfully!")
