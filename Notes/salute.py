# Write a function answer(s) which takes a string representing employees
# walking along a hallway and returns the number of
# times the employees will salute. s will contain at least 1 and at most 100
# characters, each one of -, >, or <.
#
# Languages
# =========
#
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
#
# Test cases
# ==========
#
# Inputs:
#    (string) s = ">----<"
# Output:
#    (int) 2
#
# Inputs:
#    (string) s = "<<>><"
# Output:
#    (int) 4
#
# Python
#
# ======
#
# Your code will run inside a Python 2.7.6 sandbox.
#
# Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd,
# pyexpat, select, signal, termios, thread,
# time, unicodedata, zipimport, zlib.

# the O(n) of this first solution is pretty high (I think)


def answer(s):
    count = 0
    for index, char in enumerate(list(s)):
        if char == '>':
            # We want to count how many times this '>' collides with '<'
            # While the '<' is ahead of current '>' to avoid recounting
            for place, value in enumerate(list(s)):
                if value == '<' and place > index:
                    count += 2
    return count


def answer2(s):
    count = 0
    a = 0
    for char in list(s):
        if char == '>':
            a += 2
        elif char == '<':
            count += a
    return count


print(answer2(">----<"))
print(answer2("<<>><"))
print(answer2("--->-><-><-->-"))
