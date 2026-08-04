class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums=sorted(nums)
        for n in range(len(nums)+1):
            if nums[n]==nums[n+1]:
                return nums[n]
        