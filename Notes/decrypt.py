# Write a function called answer(s) which takes in a string and returns the
# deciphered string so you can show the
# commander proof that these minions are talking about "Lance & Janice" instead
# of doing their jobs.
#
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
#     (string) s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
# Output:
#     (string) "did you see last night's episode?"
#
# Inputs:
#     (string) s = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
# Output:
#     (string) "Yeah! I can't believe Lance lost his job at the colony!!"

import string


def answer(s):
    # Add lowercase letters to dict with key(reversed alphabet)
    code = dict(zip(string.ascii_lowercase, string.ascii_lowercase[::-1]))
    return ''.join([code[i] if i.islower() else i for i in list(s)])


def answer2(s):
    return ''.join([chr((25 - ord(i) + ord('a')) + ord('a')) if i.islower()
                    else i for i in s])


print(answer2("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
print(answer2("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
