class Solution(object):
    def numIdenticalPairs(self, nums):
        
        goodPairs = 0
        visited = {}
        
        for i in nums:
            if i in visited:
                goodPairs += visited[i]
                visited[i] += 1
            else:
                visited[i] = 1
        
        return goodPairs

""" Reflection
I took some time to learn about Hash Maps and 
Brute Force then watched some videos on this particular 
problem. I have a grasp of the solution but,
can't exactly wrap my head around it. This problem was a great 
introduction to implementing dictionaries and it's specialties.
I feel like there are a lot of moving part that I unable to account 
for. I think drawing out everything will resolve that.
""" 

""" First attempt:
class Solution(object):
    def numIdenticalPairs(self, nums):
        
        goodPairs = 0
        
        for i in nums:
            for j in nums:
                if nums[i] == nums[j] & i < j:
                    goodPairs += 1
        
        return goodPairs
"""

""" Reflection
I had to watch a video to understand what is the 
question asking. Eventually I understood what is the goal.
When I run the code it is acceptable but, when I
submit it it does not pass the test case of 
[1, 1, 1, 1]. I realized there are some concepts
I am unaware of such as Brute Force and Hash Maps.
I will need to take some time to look into the concepts.
""" 