"""
------------------------------------------------------------
Python Journey - PY-010
Challenge: Find the Second Largest Number

Objective:
    Find the second largest unique number in a list.

Rules:
    - Use a function
    - Use loops
    - Use conditional statements
    - Do not use max()
    - Do not use sort()
    - Do not use sorted()
    - Do not use set()
    - Handle negative numbers
    - Handle duplicate numbers
    - Handle lists with fewer than two unique numbers

Difficulty:
    🥉 Bronze+

Author:
    Dasun
------------------------------------------------------------
"""


def find_second_largest(numbers):
    largest_number = float("-inf")
    second_largest_number = float("-inf")

    for num in numbers:

        # If the current number is larger than
        # the current largest number
        if num > largest_number:
            # The old largest becomes the
            # second largest
            second_largest_number = largest_number

            # The current number becomes
            # the new largest
            largest_number = num

        # If the current number is not the largest
        # and is larger than the current second largest
        elif num != largest_number and num > second_largest_number:
            second_largest_number = num

    # If no second largest unique number exists,
    # return None
    if second_largest_number == float("-inf"):
        return None

    return second_largest_number


if __name__ == "__main__":
    numbers = [12, 45, 7, 89, 23, 56]

    result = find_second_largest(numbers)

    print(f"The second largest number is: {result}")
