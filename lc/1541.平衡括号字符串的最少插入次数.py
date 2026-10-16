#
# @lc app=leetcode.cn id=1541 lang=python3
#
# [1541] 平衡括号字符串的最少插入次数
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        need = 0 # 我还欠多少个右括号
        for ch in s:
            if ch == '(':
                if need % 2 == 1: 
                    # 出现左括号了，但是前面的右括号少一个，需要加一个
                    res += 1
                    need -= 1
                need += 2
            else:
                need -= 1
                if need < 0:
                    res += 1
                    need += 2
        return res + need
            
        
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    testcase = ")))))))"
    print(s.minInsertions(testcase))