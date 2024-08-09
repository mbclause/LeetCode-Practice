"""
don't need the longest common subsequence, just see if t contains s

both strings lowercase

corner cases: 1 or both strings empty, 
s is longer than t


brute force:

loop through each char in s, if char is not in t return false,

if found, save index in t and only search through remaining chars in subsequent loops

how 

def func(s, t):
	if |s| < 1 or |t| < 1:
		return false
		
	if |s| > |t|:
		return false
		
		
	start = 0
	contains = False
	
	for c1 in s:
		for c2 in t from t[start] to t[n]:
			if c1 == c2:
				start = c2.index
				contains = True
				break
			if contains == False:
				return False
			else:
				contains = False
				
		return True
		

worst case is when s is a subsequence of t but there are lots of chars which aren't a part of itin between each letter in the subsequence
Analysis O(n*m)

bottleneck is inner for loop, would a 2 pointer approach work, start from the beginning of s and the end of t? No
"""


def isSub(s, t):
        if len(s) < 1:
            return True
        if len(t) < 1:
            return False
        if len(s) > len(t):
            return False
        start = 0
        contains = False
        for c1 in s:
            for i in range(start, len(t)):
                if c1 == t[i]:
                    start = i + 1
                    contains = True
                    break
            if contains == False:
                return False
            else:
                contains = False
        return True

print(isSub("abc", "ahbgdc"))


"""
can be done in O(n) time using recurion, as seen on Geeks for Geeks

def isSubSequence(string1, string2, m, n):
    # Base Cases
    if m == 0:
        return True
    if n == 0:
        return False
 
    # If last characters of two
    # strings are matching
    if string1[m-1] == string2[n-1]:
        return isSubSequence(string1, string2, m-1, n-1)
 
    # If last characters are not matching
    return isSubSequence(string1, string2, m, n-1)

"""