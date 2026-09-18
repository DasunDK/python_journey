"""
------------------------------------------------------------
Python Journey - PY-016
Challenge: Find the First Non-Repeating Number

Objective:
    Find the first number that appears exactly once
    in a list.

Rules:
    - Use a function
    - Use loops
    - Use conditional statements
    - Do not use count()
    - Do not use Counter
    - Do not use set()
    - Do not use dictionaries
    - Do not use sort()
    - Do not use sorted()
    - Do not use list comprehensions
    - Do not use external libraries
    - Preserve the original order
    - Handle negative numbers
    - Return None if every number is repeated

Difficulty:
    🥉 Bronze+

Author:
    Dasun
------------------------------------------------------------
"""


def find_first_non_repeating(numbers):
    # TODO:
    # Loop through the numbers in their original order.

    # TODO:
    # For each number, count how many times
    # it appears in the list.
    #
    # Do NOT use count().

    # TODO:
    # If the number appears exactly once,
    # return it immediately.
    #
    # Remember:
    # We need the FIRST non-repeating number.

    # TODO:
    # If no number appears exactly once,
    # return None.

    for num in numbers:
        count = 0
        for i in range(len(numbers)):
            if num == numbers[i]:
                count += 1
            if count > 1:
                break

        if count == 1:
            return num


if __name__ == "__main__":
    numbers = [10, 20, 10, 30, 20, 40]

    result = find_first_non_repeating(numbers)

    print(f"Numbers: {numbers}")
    print(f"First non-repeating number: {result}")
