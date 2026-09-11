class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=left+right//2
            if nums[mid]<nums[right]:
                right-=1
            elif nums[mid]>nums[right]:
                left+=1
            else:
                return nums[mid]    