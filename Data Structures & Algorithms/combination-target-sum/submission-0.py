class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, curr):
            total = sum(curr)
            if total == target:
                result.append(curr[:])
                return
            
            if total > target or index >= len(nums):
                return

            curr.append(nums[index])
            backtrack(index, curr)
            curr.pop()

            backtrack(index+1, curr)

        backtrack(0, [])
        return result       
            
