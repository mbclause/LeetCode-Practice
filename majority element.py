"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

"""
what does "you may assume the majority element always exists in the array"? there are never ties?

brute force: loop through nums, store each unique element in a different array D
for each element in D, loop through nums, store count in a new array C
return element with highest count in D



def majorityElement(nums):
    let D be an empty list
    let C be an empty list

    D.add(nums[0])

    for x in nums from 2 to n:
        if x is not in D:
            D.add(x)
        
    for x in D:
        C[i] = 0
        for y in nums:
            if x == y:
                C[i]++

    maxIndex = 0
    
    for i in range(0, len(C))
        if C[i] > C[maxIndex]:
            maxIndex = i
    
    return D[maxIndex]

Analysis:
O(n^2)
bottleneck is first 2 outer for loops
"""

def majorityElement(nums):
    D = []
    C = []

    for x in nums:
        if x not in D:
            D.append(x)

    for i in range(0, len(D)):
        C.append(0)
        for x in nums:
            if x == D[i]:
                C[i] += 1

    maxIndex = 0

    for i in range(0, len(C)):
        if C[i] > C[maxIndex]:
            maxIndex = i

    return D[maxIndex]




"""
improved algorithm: only one pass through array, use hash tables
key = nums[i], value = nums[i].count

def improvedMajElement(nums):
    L = HashMap()

    for x in nums:
        if L.contains(x) == false:
            L.insert(x, 1)
        
        else:
           increment value for x by 1

    return key with largest value in L 

O(n)
"""


def improvedAlg(nums):
    L = {}

    for x in nums:
        if L.get(x) == None:
            L[x] = 1

        else:
            val = L.get(x)
            val += 1
            L.update({x: val})

    v = list(L.values())

    k = list(L.keys())

    return k[v.index(max(v))]


nums = [2,2,1,1,1,2,2]

print(improvedAlg(nums))


"""
turns out the Boyer Moore majority vote algorithm is the best. it only takes O(1) space
"""
