class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {}

        for n in nums:
            freq_count[n] = freq_count.get(n, 0) + 1

        freq_sorted = dict(sorted(freq_count.items(), key = lambda item: item[1], reverse = True))

        k_nums = []
        count = 0
        for key, v in freq_sorted.items():
            if count < k:
                k_nums.append(key)
                count += 1

        return k_nums
