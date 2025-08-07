"""
Assume s is a string of lower case characters. Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""


def longest_substring(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    current_max_substring = ''
    for i in range(len(s)):
        current_substring = s[i]
        for j in range(i + 1, len(s)):
            if alphabet.index(current_substring[-1]) <= alphabet.index(s[j]):
                current_substring += s[j]
            else:
                break
        if len(current_substring) > len(current_max_substring):
            current_max_substring = current_substring
    print(current_max_substring)


def test():
    longest_substring('azcbobobegghakl')
    longest_substring('abcbcd')


test()