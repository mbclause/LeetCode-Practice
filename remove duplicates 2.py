"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

"""
brute force idea:
keep a count variable that counts the number of same variables, if it exceeds 2, delete it

def removeDuplicates(nums):
    count = 1
    prev = nums[0]
    k = len(nums)
    i = 1
    increment = true
    while i < k:
        if nums[i] == prev:
            count += 1

        else:
            count = 1

        if count > 2:
            nums.pop(i)
            nums.insert(i, None)
            increment = false
            k -= 1

        else:
            increment = true

        prev = nums[i]

        if increment = true:
            i+=1

    return k

    
algorithm 2:
make a pass through array, storing the counts for each number


"""



def removeDuplicates(nums):
    count = 1
    prev = nums[0]
    k = len(nums)
    i = 1
    increment = True

    while i < k:
        if nums[i] == prev:
            count += 1
        else:
            count = 1

        if count > 2:
            nums.pop(i)
            nums.insert(k - 1, None)
            increment = False
            k -= 1
        else:
            increment = True

        if increment:
            prev = nums[i]
            i += 1
        else:
            prev = nums[i - 1]

    return k


nums = [1,1,1,2,2,3]

result = removeDuplicates(nums)

print(result, nums)


"""
more efficient algorithm from chat GPT

def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    j = 2  # Pointer to place the next unique element
    for i in range(2, len(nums)):
        if nums[i] != nums[j - 2]:  # Compare with the element at j-2
            nums[j] = nums[i]
            j += 1

    return j
"""