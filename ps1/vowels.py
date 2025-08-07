"""
Assume s is a string of lower case characters. Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
"""


def vowels(s):
    vowels_list = 'aeiouAEIOU'
    vowel_count = 0
    for i in s:
        if i in vowels_list:
            vowel_count += 1
    print("Number of vowels: ", vowel_count)


def tests():
    vowels('azcbobobegghakl')


tests()