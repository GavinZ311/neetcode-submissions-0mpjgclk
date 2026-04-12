# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0
        e = len(pairs)-1
        self.qSort(pairs, s, e)
        return pairs
    
    def qSort(self, pairs: List[Pair], s, e) -> List[Pair]:
        if e-s+1 <= 1:
            return pairs
        pivot = pairs[e].key
        left = s

        for i in range(s,e):
            if pairs[i].key < pivot:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1
        
        tmp = pairs[e]
        pairs[e] = pairs[left]
        pairs[left] = tmp

        self.qSort(pairs, s, left-1)
        self.qSort(pairs, left+1, e)

        return pairs

        