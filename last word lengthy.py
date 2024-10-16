"""
corner cases: string ends with a space, multiple spaces between words, string can't be empty, string of all spaces, no spaces

brute force:
start with the end of the string, copy characters until you hit a space
if you start with a space, keep going until you hit an letter

def lastWord(s):
    if last char is space:
        Loop from s.back until a letter is reached:
            if s.front is reached:
                return 0
    Loop from s.back until a ' ' is reached or s.front is reached:
        count++
    return count
"""

def lastWord(s):
    i = len(s) - 1

    c = s[i]

    count = 0

    while c.isspace():
        if i == 0:
            return 0
        i -= 1
        c = s[i]

    while c.isspace() == False:
        count += 1
        if i == 0:
            return count
        i -= 1
        c = s[i]

    return count

print(lastWord("Hello World"))

print(lastWord("   fly me   to   the moon  "))

print(lastWord("luffy is still joyboy"))

    