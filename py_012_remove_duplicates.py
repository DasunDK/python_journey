"""
------------------------------------------------------------
Python Journey - PY-012
Challenge: Remove Duplicate Numbers

Objective:
    Create a new list containing only unique numbers
    while preserving their original order.

Rules:
    - Use a function
    - Use a loop
    - Create a new result list
    - Do not use set()
    - Do not use dict
    - Do not use count()
    - Do not use Counter
    - Do not sort()
    - Do not modify the original list
    - Preserve the original order

Difficulty:
    🥉 Bronze+

Author:
    Dasun
------------------------------------------------------------
"""


def remove_duplicates(numbers):
    # TODO:
    # Create an empty list that will store
    # the unique numbers.

    # TODO:
    # Loop through every number in the list.

    # TODO:
    # Check whether the current number is
    # already inside your result list.
    #
    # If it is NOT there, add it.

    # TODO:
    # Remember:
    #
    # [10, 20, 10, 30]
    #
    # The second 10 should NOT be added.

    # TODO:
    # Return your new list.
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    return unique_numbers


if __name__ == "__main__":
    numbers = [10, 20, 10, 30, 20, 40, 10]

    result = remove_duplicates(numbers)

    print(f"Original list: {numbers}")
    print(f"Unique list: {result}")
