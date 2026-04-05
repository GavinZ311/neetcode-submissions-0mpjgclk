# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mSort(pairs, 0, len(pairs))

    def mSort(self, pairs: List[Pair], s, e) -> List[Pair]:
        if e-s+1<=1:
            return pairs
        
        m = (s+e)//2

        self.mSort(pairs, s, m)
        self.mSort(pairs, m+1, e)

        self.merge(pairs, s, m, e)

        return pairs

    
    def merge(self, pairs: List[Pair], s, m, e) -> List[Pair]:
        left = pairs[s:m+1]
        right = pairs[m+1:e+1]
        l = 0
        r = 0
        i = s

        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                pairs[i] = left[l]
                l+=1
            else:
                pairs[i] = right[r]
                r+=1
            i+=1

        while l < len(left):
            pairs[i] = left[l]
            i+=1
            l+=1
        while r < len(right):
            pairs[i] = right[r]
            i+=1
            r+=1



