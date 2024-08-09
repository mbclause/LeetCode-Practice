"""
corner cases: array can't be empty, first element is zero, nums has size 1, 

similar algorithms: can't think of any

brute force algorithm:
keep iterating through all possible jumps until either we've tried all of them or we reach the last element, then break

let's do a recursive approach? make a jump, then pass the rest of the array from the element you landed on
got to check that we don't go out of bounds

base case is we've iterated through all the possibilites or we've reached the end of array

wait a second, if there are no zeros in the array, we can definitely reach the end, if there are zeros, 
we need to be able to jump over them, if we can't then it's false

new algorithm, find the zeros, check the preceding elements, if the element is greater than the distance from the zero, 
then we can jump over it

don't know if this is faster or not


def jumpGame(nums):
    if len(nums) < 2:
		return true
		
	if nums[0] == 0:
		return false

    if nums.count(0) == 0:
        return true
		
	for x in range(1, nums[0]):
		if x == len(nums) - 1:
			return true
		elif jumpRecurse(nums, x) == True:
			return true
				
	return false
		
def jumpRecurse(nums, start):
	if nums[start] == 0:
		return false
		
	for x in range(1, nums[start]):
		if start + x == len(nums) - 1:
			return true
		elif jumpRecurse(nums, start + x) == True:
			return true
				
	return false

analysis needs master theorum

for loop runs n times worst case


T(n) = 
"""





class Solution(object):
    def jumpRecurse(self, nums, start):
        if start == len(nums) - 1:
            return True

        if nums[start] == 0:
            return False

        for x in range(1, nums[start] + 1):  
            if self.jumpRecurse(nums, start + x):
                return True
        return False

    def canJump(self, nums):
        if len(nums) < 2:
            return True  
        return self.jumpRecurse(nums, 0)  


		



nums = [2,0,0]

solution = Solution()

print(solution.canJump(nums))