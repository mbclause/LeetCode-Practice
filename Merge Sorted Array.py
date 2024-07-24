'''
corner cases:
one of the arrays is empty


brute force:
idea: two nested loops for each array

def func(num1, nums2, m, n):
numSorted = m
for num1 in nums1:
			for num2 in nums2:
						if i >= numSorted:
								replace num1 with num2
						else:
							if num2 < num1:
									shift elements in nums1 right 1
									replace num1 with num2
									
							numSorted++
						
O(n*m)
'''




def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        numSorted = m

        i = j = 0

        for y in nums2:
            for x in nums1:
                if i >= numSorted:
                    nums1[i] = y
                    numSorted+=1
                else:
                    if y < x:
                        nums1 = nums1[:i] + nums2[j:j+1] + nums1[i:-2]
                        numSorted+=1
                i+=1
            j+=1


nums1 = [1,2,3,0,0,0]

nums2 = [2,5,6]

merge(nums1, 3, nums2, 3)

print(nums1)


def test(nums1, nums2):
    i = 2
    j = 0
    return nums1[:i] + nums2[j:j+1] + nums1[i:-1]



