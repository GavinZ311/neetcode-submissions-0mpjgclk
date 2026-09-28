class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total = len(nums1) + len(nums2)
        half = total // 2

        #Making nums1 to have less length
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        l, r = 0, len(nums1) - 1

        while True:
            mid = (l+r)//2 
            j = half - mid - 2

            n1left = nums1[mid] if mid >= 0 else float('-infinity')
            n1right = nums1[mid + 1] if mid+1 < len(nums1) else float('infinity')

            n2left = nums2[j] if j >= 0 else float('-infinity')
            n2right = nums2[j+1] if j + 1 < len(nums2) else float('infinity')

            if n1left <= n2right and n2left <= n1right:
                if total % 2 == 1:
                    return min(n1right, n2right) 
                else:
                    return (max(n1left, n2left) + min(n1right, n2right)) / 2
            elif n1left > n2right:
                r = mid - 1
            else:
                l = mid + 1
