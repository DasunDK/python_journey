"""
------------------------------------------------------------
Python Journey - PY-004
Challenge: Find the Largest Number

Objective:
    Find the largest number in a list without using
    Python's built-in max() or sorting functions.

Rules:
    - Use variables
    - Use a loop
    - Use conditional statements
    - Do not use max(), sort(), or sorted()

Skills Practiced:
    - Lists
    - Traversing collections
    - Comparison operators
    - Algorithmic thinking

Difficulty:
    🥉 Bronze

Author:
    Dasun
------------------------------------------------------------
"""

def find_the_largest_num(numbers):
    largest_num = numbers[0]
    
    for num in numbers:
        if num > largest_num:
            largest_num = num
               
    return largest_num

if __name__ == "__main__":
    numbers = [12, 45, 7, 89, 23, 56]
    result = find_the_largest_num(numbers)
    print (f"The largest number is: {result}")