#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        def find(n: int) -> int:
            if d[n] != n:
                d[n] = find(d[n])
            return d[n]

        def union(x: int, y: int) -> None:
            px = find(x)
            py = find(y)
            if px == py:
                return
            if px > py:
                px, py = py, px
            d[py] = px
            cnt[px] += cnt[py]

        d = {}
        cnt = {}
        for n in nums:
            if n not in d: # 还没有这个数
                d[n] = n
                cnt[n] = 1
                if (n + 1) in d:
                    union(n, n + 1)
                if (n - 1) in d:
                    union(n - 1, n)

        maxl = 0
        for val in cnt.values():
            maxl = max(val, maxl)
        return maxl

            

        
# @lc code=end



if __name__ == "__main__":
    s = Solution()
    testcase = [-1,1,0]
    print(s.longestConsecutive(testcase))