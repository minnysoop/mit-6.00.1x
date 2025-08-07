"""
Assume s is a string of lower case characters. Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
"""


def bob(s):
    match = 'bob'
    bob_count = 0
    for i in range(0, len(s)):
        if s[i] == match[0] and i + len(match) - 1 < len(s):
            accumulated_str = ''
            for j in range(i, i + len(match)):
                accumulated_str += s[j]
            if accumulated_str == match:
                bob_count += 1
    print("Number of times bob occurs is: ", bob_count)


def tests():
    bob('azcbobobegghakl')
    bob('ogoboobobobsobobobobb')
    bob('obzbboobbobbwboobobbobob')
    bob('ejobobbobbboobbhfboboocbobbobobbobb')
    bob('bobobobobobobobobobob')


tests()