"""
By: Mahad Osman
Exercise: Python Syntax 
Date: Nov 4th, 2022
"""
def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  

    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.

    # YOUR CODE HERE
    i = 0
    sum = 0
    while i < len(nums):
      sum = sum + nums[i]
      i = i + 1
    
    return sum


  
print("sum_nums returned", sum_nums([1, 2, 3, 4]))
