'''
本题在上一题的基础上加大难度，允许进行最多两次买卖。
如prices=[3,3,5,0,0,3,1,4] 
输出为6((3-0)+(4-1))。本题我没有什么思路，于是借鉴discuss中的方法。
它的方法遍历两个prices。第一次遍历维护一个profits数组每一次添加的元素为前i
天卖时能获得到的最大利益；第二次遍历时维护一个total_max变量，
从后往前遍历。每一次遍历i表示第i天买能获得的最大收益。total_max为此值加上
profits[i]。因此total_max可以表示总最大收益。
本题时间复杂度O(n)。运行时间64ms。
'''
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        profits = []
        max_profit = 0 #当前最大收益
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min) 
            profits.append(max_profit)

        total_max = 0    
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])

        return total_max
