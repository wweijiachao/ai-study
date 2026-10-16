#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for ch in s:
            if len(res) == 0 or res[-1] != ch:
                res.append(ch)
            else:
                res.pop()
        return ''.join(res)
                
        
# @lc code=end


