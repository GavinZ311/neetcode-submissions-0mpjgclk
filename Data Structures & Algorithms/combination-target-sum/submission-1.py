class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        numsList = []

        def backtrack(nums, index):
            if sum(numsList) == target:
                res.append(numsList[:])
                return
            
            if sum(numsList)>target or index >= len(nums):
                return
            
            numsList.append(nums[index])
            backtrack(nums, index)
            numsList.pop()
            backtrack(nums, index+1)
        
        backtrack(nums, 0)
        return res
            
