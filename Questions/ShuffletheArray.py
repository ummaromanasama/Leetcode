class Solution(object):
    def shuffle(self, nums, n):
        
        newNums = []
        
        for i in range(0, n):
            newNums.append(nums[i])
            newNums.append(nums[i+n])
        return newNums
    
""" Reflection
For this problem, I paired program for the coding portion.
I spent some time writing out my approach and writing pseudocode.
My thought process was very wordy compared to the final submission.
Having another perspective made the experience of coding more 
enlightening and efficient.
"""