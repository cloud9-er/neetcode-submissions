class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        i=[]
        sort=[]
        while len(sort)<2:
            smallest=min(prices)
            sort.append(smallest)
            prices.remove(smallest)
            s=sum(sort)
            print(sort)
        if s>money:
            return money
        else:
            change=money-s
            return change
        