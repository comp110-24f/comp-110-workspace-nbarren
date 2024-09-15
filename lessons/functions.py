"""Practice with Functions"""

from random import randint


# Defining a Function
def sum(num1: int, num2: int) -> int:
    """Return sum of two numbers."""
    return num1 + num2


# Call the function
# print(sum(num1=1, num2=10))  # 1 and 10 are arguments
sum(num1=randint(1, 10), num2=randint(1, 10))
