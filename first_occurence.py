"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

 

Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.


    
corner cases: haystack and needle can't be empty, if needle is longer than haystack, then return -1

Brute force method:

loop through haystack until we find the first char of needle (if we finish, than return -1) and save this index i
then, for each char in needle, check that the next char in haystack matches, if we get through needle, return i, otherwise return -1

def first_occurence(needle, haystack):
    if |needle| > |haystack|:
        return -1

    cn = first char of needle

    i = -1

    for ch in haystack:
        if cn == ch:
            i = ch index
            break
            
    if i == -1:
        return -1

    if i + |needle| > |haystack|:
        return -1

    index = 0    
    
    for ch in haystack from i to (i + |needle|):
        if ch != needle[index]:
            return -1
        index++

    return i
---------------------
ATTEMPT NO 2
----------------------

loop through haystack and check for each occurence of needle[0], save the indices in the list candidates

if candidates is empty, return -1

for each index in candidates:
    loop through needle starting at 0 and haystack starting at index, check if the chars match
        if they don't match, continue to next index
    
    if we get through loop, return index

return -1 if we loop through all indices without returning


time complexity: O(n*M), 
"""


def first_occurence(haystack, needle):
    if len(needle) > len(haystack):
        return -1

    candidates = []

    cn = needle[0]

    i = 0

    for ch in haystack:
        if cn == ch:
            candidates.append(i)
        i += 1
            
    if len(candidates) < 1:
        return -1

    match = False

    for index in candidates:
        i = index

        for c in needle:
            if i >= len(haystack):
                match = False
                break

            if c != haystack[i]:
                match = False
                break

            match = True

            i += 1

        if match == True:
            return index

    return -1



print(first_occurence("sadbutsad", "sad"))

print(first_occurence("leetcode", "leeto"))

print(first_occurence("mississippi", "issip"))