class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        totalCandies = []
        greatestCandies = []
        addCandies = 0
        highestCandy = max(candies)
        
        for candy in candies:
            addCandies = candy + extraCandies
            totalCandies.append(addCandies)
        
        for num in totalCandies:
            if num >= highestCandy:
                greatestCandies.append(True)
            else:
                greatestCandies.append(False)

        return greatestCandies
        
""" Reflection
Outlining my approach to this problem helped me out a lot.
I was appending the True and False values as strings 
for the longest time which made me second guess my code
for a moment. My code made sense as I reviewed it line 
by line and figured that I wasn't providing Leetcode 
with the expected type.
"""