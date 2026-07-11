class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        st=set(nums)
        if len(nums)<=1:
            return nums
        if len(st)==len(nums):
            return nums
        else:
            lst=set()
            for num in nums:
                if nums.count(num)>1:
                    lst.add(num)
            return list(lst)
                

        