#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l, r = -1, len(nums)
        if r == 0:
            return [-1, -1]
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m
            else:
                r = m
        r1 = r
        r = len(nums)
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m
        r2 = l
        if (r1 > r2):
            return [-1, -1]
        return [r1, r2]

        
            
        
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    testcase = [1]
    print(s.searchRange([5,7,7,8,8,10],6))