class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max1 = 0
            for a in range(len(arr)-i-1):
                if arr[a+i+1]>=max1:
                    max1=arr[a+i+1]
            arr[i] = max1
        arr[-1] = -1
        return arr