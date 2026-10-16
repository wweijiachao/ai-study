#
# @lc app=leetcode.cn id=2913 lang=python3
#
# [2913] 子数组不同元素数目的平方和 I
#

# @lc code=start
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        res = 0
        s = set()
        for i in range(len(nums)):
            cnt = 0
            s.clear()
            for j in range(i, len(nums)):
                if nums[j] not in s:
                    s.add(nums[j])
                    cnt += 1
                res += cnt ** 2
        return res
        
# @lc code=end
