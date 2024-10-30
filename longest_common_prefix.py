"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.


A prefix are the starting chars of the word

Example: strs = [crap, car, cone]

output: "c"

Corner Cases:
a string can be empty "", which would mean the program would automatically output ""
what if there's only 1 string, then return that string


Brute force:

let shortest = strs[0]

for word in strs:
    if len(word) < len(shortest)
    max = word

let result = ""

For i, ci in zip(len(shortest) - 1, shortest):
    for str in strs:
        if str[i] != ci:
            return result
    result = result + ci

return result

O(n^2) worst case, all words are exactly the same
"""

def longest_prefix(strs):
    # if there's only one string in the list, return that string
    if len(strs) < 2:
        return strs[0]

    # set shortest to first string in list
    shortest = strs[0]

    # find shortest string in list
    for word in strs:
        if len(word) < len(shortest):
            shortest = word

    # if shortest string is empty, return empty string
    if len(shortest) < 1:
        return ""
    
    # init result
    result = ""

    # loop through each char in shortest
    for ci, i in zip(shortest, range(0, len(shortest))):
        # compare ci of shortest with cis of the other strings
        for str in strs:
            # return result if they don't match
            if str[i] != ci:
                return result
        # otherwise, add ci to result
        result = result + ci

    # if we get through loop, that means shortest is longest prefix, return it
    return result


print(longest_prefix(["flower","flow","flight"]))

print(longest_prefix(["dog","racecar","car"]))

print(longest_prefix(["dog","racecar","car", ""]))

print(longest_prefix(["caar"]))


"""
improved algorithm: inner for loop is bottleneck, how to get rid of it?

hash table? find shortest string, then put each string in hash_map

divide and conquer 


from GeeksforGeeks.com

def longest_common_prefix(strs):
    # If the list is empty, return "-1"
    if not strs:
        return "-1"

    # Sort the list of strings
    strs.sort()

    # Get the first and last strings after sorting
    first = strs[0]
    last = strs[-1]
    min_length = min(len(first), len(last))

    i = 0
    # Find the common prefix between the first
    # and last strings
    while i < min_length and first[i] == last[i]:
        i += 1

    # Check if there's no common prefix
    if i == 0:
        return "-1"

    # Return the common prefix
    return first[:i]
"""
