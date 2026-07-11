class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        st=set(nums)
        if len(nums)<=1:
            return nums
        if len(st)==len(nums):
            return list(k)
        else:
          lst=sorted(st,key=lambda x:nums.count(x),reverse=True)
          t=lst[0:k]
          return t

                

        