"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

 

Constraints:

    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.



Corner cases: strings have different lengths, b is longer than a,


Algorithm: 
if a and b have different lengths, pad the rest of the shorter string with zeros on the left hand side

if 1 and 1: result is 0 and carry over a 1 bit to next place (have a bool carry_bit, set it to true)
if 1 and 0: result is 1
if 0 and 0: result is 0
if 1 and 1 and carry: result is 1 and carry_bit = true


"""

def binary_add(a, b):
    if len(a) >= len(b):
        long = a
        short = b
    else:
        long = b
        short = a

    if len(a) != len(b):
        num_zeros = len(long) - len(short)
        short = ("0" * num_zeros) + short

    carry = False

    result = ""

    for bit1,bit2 in zip(long[::-1], short[::-1]):
        if carry:
            if bit1 == "1" or bit2 == "1":
                if bit1 == "1" and bit2 == "1": #1+1+1
                    bit = "1"
                else: # 1+1+0
                    bit = "0"
                carry = True
            else: # 1+0+0
                bit = "1"
                carry = False
        else:
            if bit1 == "1" or bit2 == "1":
                if bit1 == "1" and bit2 == "1": #1+1
                    bit = "0"
                    carry = True
                else: # 1+0
                    bit = "1"
                    carry = False
            else: # 0+0
                bit = "0"
                carry = False

        result = bit + result

    if carry:
        result = "1" + result

    return result


print(binary_add("11","1"))

print(binary_add("1010", "1011"))


"""
better Python program

def add_binary(bin1, bin2):
    # Convert binary strings to integers, add them, and convert the sum back to binary
    sum_decimal = int(bin1, 2) + int(bin2, 2)
    # Format the result to binary and remove the '0b' prefix
    return bin(sum_decimal)[2:]

# Example usage
bin1 = "1010"
bin2 = "1101"
result = add_binary(bin1, bin2)
print(f"The sum of {bin1} and {bin2} is: {result}")
"""
                


