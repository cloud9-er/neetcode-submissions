class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        longest=1
        current=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                current+=1
            else:
                longest=max(current,longest)
                current=1
        return max(current,longest)