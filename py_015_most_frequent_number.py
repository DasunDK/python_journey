"""
------------------------------------------------------------
Python Journey - PY-015
Challenge: Find the Most Frequent Number

Objective:
    Find the number that appears the most times
    in a list.

Rules:
    - Use a function
    - Use loops
    - Use conditional statements
    - Do not use count()
    - Do not use Counter
    - Do not use max()
    - Do not use set()
    - Do not use dictionaries
    - Do not use sort()
    - Do not use sorted()
    - Do not use list comprehensions
    - Do not use external libraries
    - Handle negative numbers
    - Handle ties
    - If tied, return the number that appears first

Difficulty:
    🥉 Bronze+

Author:
    Dasun
------------------------------------------------------------
"""


def find_most_frequent(numbers):
    # TODO:
    # Create variables to keep track of
    # the most frequent number and its count.
    most_frequent = 0
    highest_count = 0

    # TODO:
    # Loop through the numbers.
    for i in range(len(numbers)):
        count = 0
        for j in range(len(numbers)):

            if numbers[i] == numbers[j]:
                count += 1

        if count > highest_count:
            most_frequent = numbers[i]
            highest_count = count

    return most_frequent

    # TODO:
    # For each number, count how many times
    # it appears in the list.
    #
    # Remember:
    # You cannot use count().

    # TODO:
    # If the current number has appeared
    # more times than the current highest count,
    # update your variables.

    # TODO:
    # Return the most frequent number.


if __name__ == "__main__":
    numbers = [10, 20, 10, 30, 20, 10]

    result = find_most_frequent(numbers)

    print(f"Numbers: {numbers}")
    print(f"Most frequent number: {result}")
