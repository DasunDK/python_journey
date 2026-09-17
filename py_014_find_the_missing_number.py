"""
------------------------------------------------------------
Python Journey - PY-014
Challenge: Find the Missing Number

Objective:
    Find the missing number from a list containing
    numbers from 1 to n.

Rules:
    - Use a function
    - Use loops
    - Do not use sum()
    - Do not use set()
    - Do not use sort()
    - Do not use sorted()
    - Do not use list comprehensions
    - Do not use external libraries
    - Exactly one number is missing

Difficulty:
    🥉 Bronze+

Author:
    Dasun
------------------------------------------------------------
"""


def find_missing_number(numbers):
    # TODO:
    # First, determine what the largest expected
    # number should be.
    #
    # Remember:
    # If the list has 4 numbers and one is missing,
    # the complete sequence contains 5 numbers.

    # TODO:
    # Calculate the expected total manually
    # using a loop.
    #
    # Do NOT use sum().

    # TODO:
    # Calculate the actual total of the numbers
    # in the list using another loop.

    # TODO:
    # The difference between the expected total
    # and actual total is the missing number.

    expected_total = 0
    actual_total = 0

    # calculate the expected total
    for i in range(1, len(numbers) + 2):
        expected_total += i

    # calculate the actual total
    for num in numbers:
        actual_total += num

    return expected_total - actual_total


if __name__ == "__main__":
    numbers = [1, 2, 3, 5]

    result = find_missing_number(numbers)

    print(f"Numbers: {numbers}")
    print(f"Missing number: {result}")
