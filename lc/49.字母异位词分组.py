#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def label(s) -> str:
            return tuple(sorted(s))

        d = {}
        for s in strs:
            l = label(s)
            if l not in d:
                d[l] = []
            d[l].append(s)
        return list(d.values())
        
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    testcase = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(testcase))