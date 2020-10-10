class Solution(object):
    def numJewelsInStones(self, J, S):
    
        return sum([s in J for s in S])

""" Reflection
I was able to breakdown what was required for the
problem but had a hard time to piece it together.
The in keyword took time to get used to and was 
interesting to see how it played out.
""" 