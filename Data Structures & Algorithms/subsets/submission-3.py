class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        numList = []

        def backtrack(index):
            if index >= len(nums):
                res.append(numList[:])
                return

            numList.append(nums[index])
            backtrack(index+1)
            numList.pop()
            backtrack(index+1)

        backtrack(0)
        return res
            