#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        for ch in t:
            if ch not in d:
                return False
            else:
                d[ch] = d.get(ch) - 1
        for value in d.values():
            if value != 0:
                return False
        return True
        
# @lc code=end

