#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        i, j = -1, len(nums)
        while i + 1 < j:
            m = (i + j) // 2
            if nums[m] <= nums[-1]:
                j = m
            else:
                i = m
        return nums[j]
        
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    testcase = [11,13,15,17]
    print(s.findMin(testcase))