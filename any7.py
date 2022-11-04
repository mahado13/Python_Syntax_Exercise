"""
By: Mahad Osman
Exercise: Python Syntax 
Date: Nov 4th, 2022
"""
def any7(nums):
    """Are any of these numbers a 7? (True/False)"""


    # YOUR CODE HERE 
    i = 0
    while i <len(nums):
        if(nums[i] ==7):
            return True
        elif(i == len(nums) -1):
            return False
        else: 
            print(i)
            i = i+ 1
    # for num in nums:
    #     if(num == 7):
    #         return True
    #     else:
    #         return False

print("should be true:", any7([1, 2, 7, 4, 5]))
print("should be false:", any7([1, 2, 4, 5]))

