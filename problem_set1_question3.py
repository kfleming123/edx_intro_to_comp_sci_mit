# Problem Set 1, Problem 3
"""
Prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print:
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print:
Longest substring in alphabetical order is: abc
"""

def alph_substring(s):
    ans_string = s[0]
    # Loop over all possible lengths of a substring
    for i in range(2, len(s) + 1):
        index_1 = 0
        # Loop over all possible substrings of size i
        for j in range(len(s) - i + 1):
            # Start with index = 0 and define substring as ss
            count = 0
            ss = s[index_1:index_1 + i]
            index_2 = 0
            for k in range(len(ss) - 1):
                if ss[index_2] > ss[index_2 + 1]:
                    count += 1
                index_2 += 1
                    # If in alphabetical order, update the answer string
            if count == 0:
                ans_string = ss
                break
            index_1 += 1
    print(ans_string)

alph_substring('azcbobobegghakl')