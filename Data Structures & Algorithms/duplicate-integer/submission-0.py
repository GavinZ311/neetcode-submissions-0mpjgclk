class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
            if nums_count[num] > 1:
                return True

        return False
