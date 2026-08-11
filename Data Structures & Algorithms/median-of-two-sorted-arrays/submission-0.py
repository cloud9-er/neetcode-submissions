class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=sorted(nums1+nums2)
        l=len(arr)
        mid=l//2
        if l%2==0:
            median=((arr[mid-1])+(arr[mid]))/2
            return median
        else:
            t=(l//2)
            median=arr[t]
            return int(median)
