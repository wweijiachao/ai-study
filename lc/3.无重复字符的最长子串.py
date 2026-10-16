#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        window = set()
        max_len = 0
        for j in range(len(s)):
            while s[j] in window:
                window.remove(s[i])
                i += 1
            window.add(s[j])
            max_len = max(max_len, j - i + 1)
        return max_len
        
# @lc code=end

