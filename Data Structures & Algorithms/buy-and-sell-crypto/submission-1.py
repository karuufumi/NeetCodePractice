'''
You need to BUY before SELLING 
so that's why you need the MIN Price
buy the lowest one, so possibly in the future sell with
higher price
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, profit =float('inf'),0
        for i in prices:
            if i < minPrice :
                minPrice = i
            profit = max(profit, i-minPrice)

        return profit