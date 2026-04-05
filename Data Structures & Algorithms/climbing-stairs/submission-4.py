class Solution:
    def climbStairs(self, n: int, thisdict = None) -> int:
        if thisdict is None:
            thisdict = {}
        if n <= 1:
            return 1

        if n-1 not in thisdict.keys():
            thisdict[n-1] = self.climbStairs(n-1,thisdict)
        
        if n-2 not in thisdict.keys():
            thisdict[n-2] = self.climbStairs(n-2,thisdict)

        return thisdict[n-1] + thisdict[n-2]