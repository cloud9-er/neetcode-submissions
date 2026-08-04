class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums=sorted(nums)
        for n in nums:
            if nums[n]==nums[n+1]:
                return nums[n]
        