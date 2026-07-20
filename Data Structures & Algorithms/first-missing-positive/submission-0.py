class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sort=set(nums)
        target=1
        while target in sort:
            target+=1
        return target

        