# Problem Set 1, Problem 2
"""
Prints a count of the number of times the string 'bob' occurs in string s. 
"""
def bob_count(s):
    ans = 0
    for i in range(len(s) - 2):
        if s[i:i+3] == 'bob': 
            ans += 1
    print("Number of times bob occurs is: " + str(ans))

bob_count('testinbobobgbob')