"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element 
appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order 
    they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    
    Return k.

"""

"""
corner cases: nums cannot be empty
no duplicates
all elements are the same
size = 1


brute force idea: loop through nums, store the previous element, while x == prevElement, remove x, insert null at index k

def removeDuplicates(nums):
    prev = nums[0]
    i = 1
    k = nums.size
    while i < k:
        while nums[i] == prev:
            nums.pop(i)
            nums.insert(k, None)
            k--
        prev = nums[i]
        i++
    return k

O(n)
"""



def removeDuplicates(nums):
    prev = nums[0]
    i = 1
    k = len(nums)
    while i < k:
        while nums[i] == prev:
            nums.pop(i)
            nums.insert(k, None)
            k-=1
        prev = nums[i]
        i+=1
    return k

nums = [0,0,1,1,1,2,2,3,3,4]

result = removeDuplicates(nums)

print(result, nums)