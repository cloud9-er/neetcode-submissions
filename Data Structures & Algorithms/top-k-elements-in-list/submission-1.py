class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<=1:
            return nums
        lst=set()
        for num in nums:
            if nums.count(num)>1:
                lst.add(num)
        return list(lst)

        