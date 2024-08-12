"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x 
is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

 

Constraints:

    0 <= nums.length <= 20
    -231 <= nums[i] <= 231 - 1
    All the values of nums are unique.
    nums is sorted in ascending order.


"""



"""
is this like the min set cover? integer programming? bipartite graph?

every number in the array has to be matched with one of the ranges, 

so the ranges can't cover numbers that aren't in the array

corner cases: empty array

you can have a range whose size is greater than one only for numbers that don't skip i.e. 1,2,3 but not 1,2,4

algorithm idea: loop through nums, create a new range, starting at nums[i], 
stop the range once we skip a number, then end the range at nums[i-1] and start a new range at i, 
if start and end are the same, just use the singelton range for that number. I don't see how you could make a smaller list than that.

what do we do if we reach the end of the array?

Brute force algorithm:

def range(nums):
    create new empty list Ranges

    if nums is empty:
        return Ranges

    start = nums[0]

    prev = nums[0]

    for x in nums from 1 to n:
        if x is last element in array:
            end = x
            if start == end:
                add "start" to Ranges
            else:
                add "start->end" to Ranges
        else:
            if x > prev + 1:
                end = prev
                if start == end:
                    add "start" to Ranges
                else:
                    add "start->end" to Ranges
                start = x
        prev = x

    return Ranges

O(n)

almost, got to deal with the possibility that when we reach the last element, we're still continuing a range,
what if we deal with this after we get out of the loop?

if x > prev + 1:
    same as before
    also add x to list
else:

"""

def ranges(nums):
    R = []
    if len(nums) < 1:
        return R
    if len(nums) == 1:
        R.append("%d" % (nums[0]))
        return R
    start = nums[0]

    prev = nums[0]

    for i in range(1, len(nums)):
        x = nums[i]
        if i == len(nums) - 1:
            if x > prev + 1:
                end = prev
                if start == end:
                    R.append(f"{start}")
                else:
                    R.append(f"{start}->{end}")
                R.append(f"{x}")
            else:
                end = x
                if start == end:
                    R.append(f"{start}")
                else:
                    R.append(f"{start}->{end}")
        else:
            if x > prev + 1:
                end = prev
                if start == end:
                    R.append(f"{start}")
                else:
                    R.append(f"{start}->{end}")
                start = x
        prev = x

    return R

nums = [0,2]

print(ranges(nums))

nums = [0,2,3,4,6,8,9]

print(ranges(nums))