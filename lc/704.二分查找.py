#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m + 1
            else:
                j = m
        if nums[i] == target:
            return i
        return -1
        
# @lc code=end

