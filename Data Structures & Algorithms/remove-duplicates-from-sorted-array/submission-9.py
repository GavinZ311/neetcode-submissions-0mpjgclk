class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        i = len(nums)-1
        while i > 0:
            if nums[i] == nums[i-1]:
                nums.remove(nums[i-1])
                k-=1
            i-=1
        return k
            