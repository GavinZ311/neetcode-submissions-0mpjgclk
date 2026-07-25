class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for n in range(len(nums)):
        #         if i != n and nums[i] + nums[n] == target:
        #             return [i, n]
        # return []

#How to do this with a hashmap
        nums_map = {} #Val:index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_map:
                return [nums_map[diff], i]
            nums_map[n] = i
        return