import re

def isPalindrome(s):
    s = re.sub(r'\W+', '', s)
    s = re.sub(r'_+','',s)
    s = s.lower()

    if len(s) < 1:
        return True

    back = len(s) - 1
    for c in s:
        if c != s[back]:
            return False
        back-=1
    return True

s = " "

print(isPalindrome(s))