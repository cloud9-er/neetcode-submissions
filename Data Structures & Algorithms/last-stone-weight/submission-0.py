class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            x=max(stones)
            stones.remove(x)     
            y=max(stones)
            stones.remove(y)
            if x>y:
                rem=x-y
                stones.append(rem)
            elif y>x:
                rem=y-x
                stones.append(rem)
        return stones[0] 