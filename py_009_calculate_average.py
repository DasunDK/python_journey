"""
------------------------------------------------------------
Python Journey - PY-009
Challenge: Calculate Average

Objective:
    Calculate the average of numbers in a list without
    using Python's built-in sum() or len() functions.

Rules:
    - Use a function
    - Use a loop
    - Do not use sum()
    - Do not use len()
    - Calculate the total manually
    - Count the items manually
    - Handle an empty list safely
    - Return the average

Difficulty:
    🥉 Bronze

Author:
    Dasun
------------------------------------------------------------
"""


def calculate_average(numbers):
    # TODO:
    # Create a variable to store the total.
    #
    # Think about what the starting value should be.

    # TODO:
    # Create another variable to count how many
    # numbers are in the list.

    # TODO:
    # Loop through the numbers.
    #
    # During each iteration:
    # 1. Add the current number to the total.
    # 2. Increase the item count.

    # TODO:
    # Before dividing, think about this:
    #
    # What happens if numbers is an empty list?
    #
    # Avoid dividing by zero.

    # TODO:
    # Calculate and return the average.
    count = 0
    sum = 0
    for num in numbers:
        count += 1
        sum += num
    if count == 0:
        return 0
    return sum / count


if __name__ == "__main__":
    numbers = [10, 20, 30, 40]

    result = calculate_average(numbers)

    print(f"The average is: {result}")
