#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        methods = [1] * (n + 1)
        for i in range(2, n + 1):
            methods[i] = methods[i - 1] + methods[i - 2]
        return methods[n]
        
# @lc code=end

