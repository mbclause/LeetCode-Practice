"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.


Examples:
    s = "abdc"
    t = "1213"


Corner cases:
    both strings have length 1, automatically true
    can't have empty strings
    both strings consist of one char and have length longer than 1

First pass:
    create a hashmap myMap
    loop through both strings:
        if c1 is not in myMap:
            if c2 is in myMap:
                return false
            else: // c2 is not in myMap
                add <c1,c2> to myMap
        else:
            if c2 is in myMap:
                return false

    return true

O(n)
"""

#from chatGPT
def isomorphic_strings(s, t):
    if len(s) == 1:
        return True
    s_to_t = {}
    t_to_s = {}
    for c1, c2 in zip(s,t):
        if c1 in s_to_t:
            if s_to_t[c1] != c2:
                return False
        else:
            s_to_t[c1] = c2

        if c2 in t_to_s:
            if t_to_s[c2] != c1:
                return False
        else:
            t_to_s[c2] = c1
            
    return True


print(isomorphic_strings("egg", "add"))

print(isomorphic_strings("foo", "bar"))

print(isomorphic_strings("paper", "title"))

print(isomorphic_strings("abab", "baba"))