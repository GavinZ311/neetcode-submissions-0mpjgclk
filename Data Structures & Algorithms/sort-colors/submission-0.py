class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0, 0, 0]

        for i in nums:
            if i==0:
                bucket[0] = bucket[0]+1
            elif i==1:
                bucket[1] = bucket[1]+1
            else:
                bucket[2] = bucket[2]+1
        
        z = 0
        for i in range(len(bucket)):
            for j in range(bucket[i]):
                nums[z] = i
                z+=1