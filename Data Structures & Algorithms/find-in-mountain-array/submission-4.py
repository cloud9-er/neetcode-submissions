class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n=mountainArr.length()
        for index in range(n):
            if mountainArr.get(index) == target:
                return index
        return -1

        