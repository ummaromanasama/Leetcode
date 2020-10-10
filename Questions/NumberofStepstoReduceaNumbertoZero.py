class Solution(object):
    def numberOfSteps (self, num):
        ctr = 0
        while num != 0:
            if num % 2 == 0:
                ctr += 1
                num /= 2
            else:
                ctr += 1
                num -= 1
        return ctr

""" Reflection
I found this problem pretty straight forward and 
intuitive. I took the liberty to condense my 
code as much as possible since I had some spare 
time to look it over.
"""