class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        half = (len(nums1) + len(nums2))//2
        l, r = 0, len(nums1)-1

        while True:
            mid = (l+r) // 2
            j = half - mid - 2

            nums1left = nums1[mid] if 0 <= mid else float('-infinity')
            nums1right = nums1[mid + 1] if mid+1 < len(nums1) else float('infinity')

            nums2left = nums2[j] if 0 <= j else float('-infinity')
            nums2right = nums2[j+1] if j+1 < len(nums2) else float('infinity')

            if nums1left <= nums2right and nums2left <= nums1right:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(nums1right, nums2right)
                else:
                    return (min(nums1right, nums2right) + max(nums1left, nums2left))/2
            elif nums1left > nums2right:
                r = mid - 1
            else:
                l = mid + 1
        