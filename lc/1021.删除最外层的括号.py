#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        i = 0
        l = 0
        res = ''
        for j in range(len(s)):
            l += (1 if s[j] == '(' else -1)
            if l == 0:
                res += s[i + 1: j]
                i = j + 1
        return res

# @lc code=end

