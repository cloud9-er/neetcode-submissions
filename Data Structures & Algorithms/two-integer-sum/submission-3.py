class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        for i in range(length):
            for j in range(length):
                if nums[i]+nums[j]==target and i !=j:
                    m=min(i,j)
                    t=max(i,j)
                    return [m,t]
        