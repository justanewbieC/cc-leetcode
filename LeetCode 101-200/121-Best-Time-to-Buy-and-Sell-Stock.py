'''
本题给了这样一个情景。给定一个列表prices。列表中的元素price[i]表示第i天商品的价格。
要求求在哪一天买入，在哪一天卖出可以取得最大的收益。
如:prices=[7,1,5,3,6,4]，则maxProfit=6-1=5.
本题可以维护两个变量 maxProfit为最大利益；minPrice为商品最低价格。遍历prices中
的元素，不断更新这两个变量即可。
本题时间复杂度O(n)，运行时间40ms，击败100%用户
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit , minPrice = 0 , float('inf')
        for price in prices:
            minPrice = minPrice if minPrice <= price else price 
            profit = price - minPrice 
            maxProfit = maxProfit if maxProfit >= profit else profit
        return maxProfit
