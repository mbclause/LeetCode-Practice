"""
In: an aray nums and an integer val
Out: the array nums with all instances of val removed and the numbers of the these values, k. The first k elements of nums contain the original values in the array not equal to val

Corner cases: empty array,
no instances of val in array,
all elements in nums are val


Brute force approach: idea- loop through nums, if val is found, shift all of the remaining elements left one, delete the kth entry (k is set to n at the beginning of the program)

def removeElem(nums, val):
    k = nums.length()
    i = 0
    for x in nums:
        if x == val:
            nums.pop(i)
            nums.insert(k, None)
            k -= 1
        i += 1
    return k

    O(n)
"""




def removeElement(nums, val):
    k = len(nums)
    i = 0
    while i < k:
        while nums[i] == val:
            nums.pop(i)
            nums.insert(k, None)
            k -= 1
        i+=1
    return k


nums = [0,1,2,2,3,0,4,2]

val = 2

result = removeElement(nums, val)

print(result, nums)