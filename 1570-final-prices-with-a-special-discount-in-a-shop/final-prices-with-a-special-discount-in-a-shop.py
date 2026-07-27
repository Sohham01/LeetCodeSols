class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        a=[]
        for i in range(len(prices)):
            while a and (prices[a[-1]]>=prices[i]):
                prices[a.pop()]-=prices[i]
            a.append(i)
        return prices