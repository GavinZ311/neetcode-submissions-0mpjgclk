class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        countMax = 0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                countMax = max(countMax,count)
            else:
                countMax = max(countMax,count)
                count=0
        
        return countMax