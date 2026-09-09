"""
------------------------------------------------------------
Python Journey - PY-008
Challenge: Calculate the Sum of Numbers

Objective:
    Calculate the total sum of all numbers in a list
    without using Python's built-in sum() function.

Rules:
    - Use a function
    - Use a loop
    - Use a variable to accumulate the total
    - Do not use sum()
    - Do not use advanced libraries
    - Return the total

Skills Practiced:
    - Lists
    - Loops
    - Variables
    - Arithmetic operators
    - Accumulator pattern
    - Functions
    - Algorithmic thinking

Difficulty:
    🥉 Bronze

Author:
    Dasun
------------------------------------------------------------
"""


def calculate_sum(numbers):
    # TODO:
    # Create a variable to store the total.
    #
    # Think about:
    # What should the starting value be
    # before we add any numbers?

    # TODO:
    # Loop through every number in the list.
    #
    # For each number, add it to your total.

    # TODO:
    # After the loop finishes, return the total.
    count = 0
    for num in numbers:
        count += num
    return count


if __name__ == "__main__":
    numbers = [10, 20, 5, 15, 30]

    result = calculate_sum(numbers)

    print(f"The total sum is: {result}")
