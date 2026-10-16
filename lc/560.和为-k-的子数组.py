#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

from typing import List
# @lc code=start


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        d = {0 : 1}
        prefix = 0
        for n in nums:
            prefix += n
            res += d.get(prefix - k, 0)
            d[prefix] = d.get(prefix, 0) + 1
        return res
        
# @lc code=end
