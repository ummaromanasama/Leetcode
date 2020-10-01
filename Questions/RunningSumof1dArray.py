class Solution(object):

    def runningSum(self, nums):
        sums = 0
        newNums = []
        for num in nums:
            sums += num
            newNums.append(sums)
        return newNums

""" Reflection:
This is my first time working on a technical interview question.
I learned that I like to draw the problem out as I try to solve it.
I am a bit rusty with some concepts like classes and self.
I had to do a bit of Googling to get caught up.
"""