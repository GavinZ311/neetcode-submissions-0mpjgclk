class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newList = []
        for num in nums:
            newList.append(num)
        for num in nums:
            newList.append(num)
        return newList