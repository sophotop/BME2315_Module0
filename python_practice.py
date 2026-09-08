# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
INPUT N
set sum = 0
set 1st number = 0
set 2nd number = 1

Repeat N times
    Add first number to sum
    Calculator the fibonacci 
    move to the next 2 numbers

Output sum
"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # Keep tracks of how many numbers were added
total = 0 # Stores the running total 

while count < N: # While loop that repeats until we have computed the fibonacci number

    total = total + b # Add current fibonnacci number to the total

    next_value = a + b # Calculates the next fibonacci number
    a = b # Move b into a 
    b = next_value # Move next number into b 

    count = count + 1 # Increase count by 1

print(total) # Print the final total 

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.
import numpy as num

fib = [0,1,1,2,3,5,8,13,21,34]

standard_deviation = num.std(fib)

print(standard_deviation)

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

def fibonacci_sum(N):
    a=0
    b=1
    total=0
    for i in range(N):
        total = total + a 
        next_value = a + b
        a = b
        b = next_value 
    return total 

N_values = [5,10,15,20,25,30]
sum = []
for N in N_values:
    sum.append(fibonacci_sum(N))

print(sum)
# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0
    b = 1
    index = 0 # Initialize index to 0 before the while loop.

    while a <= limit: #TypeError because a and b are strings, not integers. We can't compare strings to integers.
        next_value = a + b
        a = b
        b = next_value
        index = index + 1

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_odd_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 == 1:  # This line checks if the Fibonacci number is odd. The original code was checking for even numbers, which is incorrect. We need to check for odd numbers instead.
            total += b # Add the odd Fibonacci number to the total, Original code just set total to b without adding it to the previous total. We need to accumulate the sum of odd Fibonacci numbers.
        a, b = b, a + b # Move to the next Fibonacci number 
    return total    


# Add your test cases here
print(sum_odd_fib(1))  # Expected output: 1
print(sum_odd_fib(5))  # Expected output: 5
print(sum_odd_fib(10))  # Expected output: 5
print(sum_odd_fib(20))  # Expected output: 23
print(sum_odd_fib(50))  # Expected output: 77
# %%
