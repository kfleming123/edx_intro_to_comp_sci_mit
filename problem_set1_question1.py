# Problem Set 1, Problem 1
"""
Prints a count of the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u
"""
def vowel_count(s):
    vowels = 0
    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowels += 1
    print("Number of vowels: " + str(vowels))

vowel_count('testing')