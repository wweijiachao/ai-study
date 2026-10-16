#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        pre2, pre1, cur = 0, 0, 0
        for i in range(2, len(cost) + 1):
            cur = min(
                pre2 + cost[i - 2],
                pre1 + cost[i - 1]
            )
            pre2, pre1 = pre1, cur
        return cur
            
        
# @lc code=end

