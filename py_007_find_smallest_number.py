# """
# ------------------------------------------------------------
# Python Journey - PY-007
# Challenge: Find the Smallest Number

# Objective:
#     Find the smallest number in a list without using
#     Python's built-in min() or sorting functions.

# Rules:
#     - Use a function
#     - Use a loop
#     - Use conditional statements
#     - Do not use min()
#     - Do not use sort() or sorted()
#     - Return the smallest number

# Skills Practiced:
#     - Lists
#     - Loops
#     - Comparison operators
#     - Variables
#     - Functions
#     - Algorithmic thinking

# Difficulty:
#     🥉 Bronze

# Author:
#     Dasun
# ------------------------------------------------------------
# """


def find_smallest_number(numbers):
    smallest_number = numbers[0]

    for num in numbers:
        if smallest_number > num:
            smallest_number = num

    return smallest_number


if __name__ == "__main__":
    numbers = [45, 12, 89, 7, 34, 23]

    result = find_smallest_number(numbers)

    print(f"The smallest number is: {result}")
