"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?



Corner cases:

First Pass:
    convert x to string, reverse string, loop through both, if the chars aren't equal return false.
      If you get through loop return true

O(n) time

O(n) space
"""

import math

def palindrome(x):
    s = str(x)

    rev = s[::-1]

    for c1, c2 in zip(s, rev):
        if c1 != c2:
            return False
        
    return True


print(palindrome(121))

print(palindrome(-121))

print(palindrome(10))



"""
next pass: don't convert number to string

how to get number of digits in a number? use a log base 10

loop through digits starting from the 1s place, add x[i] * 10^len to reverse_num

after loop, check if reverse_num == x, return true if yes, or false if no
"""

