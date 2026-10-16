#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = ''.join([c for c in s if c.isalnum()]).lower()
        slr = sl[::-1]
        print(sl, slr)
        return sl == slr
        
# @lc code=end

