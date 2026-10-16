#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxl = nums[0]
        dp = nums[0]
        for n in nums[1:]:
            dp = max(dp + n, n)
            maxl = max(maxl, dp)
        return maxl
        
# @lc code=end
