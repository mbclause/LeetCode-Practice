'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

 

Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].



Corner Cases:
    string can't be empty or be longer than 15 chars, it's a valid roman numeral

First Pass:

    loop through string: for each char, lookup value in dictionary and add it to total
    if char is I, X, or C, check that next char isn't one that you can subtract from, if yes, than subtract char from total
    O(n)
'''


def romanToInt(s):

    num = 0

    subtract = False

    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    if len(s) < 2:
        return romans[s[0]]

    for count, c in enumerate(s):
        if count < len(s) - 1:
            next = s[count + 1]
            if c == "I" or c == "X" or c == "C":
                if c == "I":
                    if next == "V" or next == "X":
                        subtract = True
                elif c == "X":
                    if next == "L" or next == "C":
                        subtract = True
                else:
                    if next == "D" or next == "M":
                        subtract = True

            if subtract:
                num -= romans[c]
            else:
                num += romans[c]

        else:
            num += romans[c]

        subtract = False

    return num

print(romanToInt("III"))

print(romanToInt("LVIII"))

print(romanToInt("MCMXCIV"))