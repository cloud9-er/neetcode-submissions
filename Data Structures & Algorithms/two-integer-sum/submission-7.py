class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        for i in range(l):
            for j in range(l):
                if nums[j] + nums[i] == target and nums[j] !=nums[i]:
                    smallest=min(i,j)
                    largest=max(i,j)
            return [smallest,largest]
            return []


       