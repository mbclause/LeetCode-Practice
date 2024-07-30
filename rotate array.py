"""
Problem: Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

corner cases: k = 0, array can't be empty

Brute force: 



"""

from collections import deque

def rotate(nums, k):
    D = deque(nums)
    D.rotate(k)
    nums[:] = list(D)






"""
algorithm without deque method:

create new array A, fill with n zeros
iterate through nums: for each x in nums, calculate new index as i = (i + k) % n,
store in A

"""

def improved(nums, k):
    A = [0] * len(nums)

    for i in range(0, len(nums)):
        index = (i + k) % len(nums)
        A[index] = nums[i]

    nums[:] = A

nums = [-1,-100,3,99]

rotate(nums, 2)

print(nums)


"""
O(n) time and space

best algorithm (reversal algorithm)

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def rotate(nums, k):
    n = len(nums)
    k %= n  # In case k is greater than n
    reverse(nums, 0, n - 1)    # Step 1: Reverse the entire array
    reverse(nums, 0, k - 1)    # Step 2: Reverse the first k elements
    reverse(nums, k, n - 1)    # Step 3: Reverse the remaining n - k elements
"""
