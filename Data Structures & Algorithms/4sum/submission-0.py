class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            idx = i + 1
            while idx < len(nums):
                b = nums[idx]
                if idx > i+1 and nums[idx] == nums[idx-1]:
                    idx += 1
                    continue
                
                l = idx + 1
                r = len(nums)-1

                while l < r:
                    fourSum = a + b + nums[l] + nums[r]
                    if fourSum < target:
                        l += 1
                    elif fourSum > target:
                        r -= 1
                    else:
                        res.append([a, b, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                idx += 1
        return res

                