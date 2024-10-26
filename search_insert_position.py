"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104

    
corner cases: nums can't be empty, nums are sorted, odd sized array

first pass:
if array size equals 1 and it does not contain target:
if target < pivot, return pivot - 1 (unless pivot index is 0, then return 0)
if target > pivot, return pivot + 1 (unless pivot is last index, then return last index)

pick pivot index ((last-first)//2)
if target less than nums[pivot], search left half of array
if greater than, search right half
if equal, return pivot

"""
def search_recurse(nums, target, first, last):
    if first == last:
        if nums[first] == target:
            return first
        else:
            if target < nums[first]:
                if first > 0:
                    return first
                else:
                    return 0
            else: # target > nums[first]
                return first + 1

    pivot = (last + first) // 2

    if nums[pivot] == target:
        return pivot
    elif target > nums[pivot]: #search right side
        if pivot == last:
            return search_recurse(nums, target, pivot, last)
        else:
            return search_recurse(nums, target, pivot + 1, last)
    else:
        if pivot == first:
            return search_recurse(nums, target, first, pivot)
        else:
            return search_recurse(nums, target, first, pivot - 1)


def search(nums, target):
    answer = search_recurse(nums, target, 0, len(nums) - 1)
    return answer

nums = [1,3]
target = 4

print(search(nums, target))


