class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        st=sorted(nums)
        return st[k+1]

        