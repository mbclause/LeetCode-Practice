"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters 
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

 

Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.


Notes:

similar to isSubsequence except the order does not matter

corner cases: magazine has length zero

algorithm idea: turn magazine into a hashmap/dictionary, key = the letter, value = number of times letter is in magazine
loop through ransomNote:
for each char, do a lookup in hash map, if it returns false or the count is 0, return false, otherwise, go to next char

def ransom(note, magazine):
    H = HashMap()
    for char in magazine:
        if H.contains(char):
            val = H.get(char)
            val++
            H.insert(char, val) // this should delete old entry
        else:
            H.insert(char, 1)

    for char in note:
        if H.contains(char):
            val = H.get(char)
            if val <= 0:
                return false
            else:
                val--
                H.insert(char, val)
        else:
            return false
    return true

O(n)
"""

def ransom(note, magazine):
    if len(magazine) < 1:
        return False

    H = {}
    for c in magazine:
        val = H.get(c)
        if val == None:
            H[c] = 1
        else:
            val += 1
            H[c] = val

    for c in note:
        val = H.get(c)

        if val == None or val <= 0:
            return False
        
        else:
            val -= 1
            H[c] = val

    return True


print(ransom("a", "b"))

print(ransom("aa", "ab"))

print(ransom("aa", "aab"))