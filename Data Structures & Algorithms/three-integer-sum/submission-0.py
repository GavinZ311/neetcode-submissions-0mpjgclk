class Solution:
    def pair_sum_sorted(self, nums: List[int], start:int, target: int) -> List[int]:
        i, j = start, len(nums)-1
        pairs = []
        while i < j:
            total = nums[i] + nums[j]
            if total == target:
                pairs.append([nums[i], nums[j]])
                i += 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
            elif total < target:
                i += 1
            else:
                j -= 1
        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pairs = self.pair_sum_sorted(nums, i+1, -nums[i])
            for pair in pairs:
                triplets.append([nums[i]]+pair)

        return triplets
