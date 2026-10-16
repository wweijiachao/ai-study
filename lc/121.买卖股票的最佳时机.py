#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for p in prices[1:]:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max(max_profit, 0)

        
# @lc code=end

