#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sums = sum(nums)
        r = sums
        for i in range(len(nums)):
            r -= nums[i]
            if r == sums - r - nums[i]:
                return i
        return -1
# @lc code=end
