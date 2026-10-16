#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            # 如果m在左半边
            if nums[0] <= nums[m]:
                if nums[0] <= target < nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            else: # m在右半边
                if nums[m] < target <= nums[-1]:
                    i = m + 1
                else:
                    j = m - 1
        return -1

                    
        
        
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    testcase = [4,5,6,7,0,1,2]
    print(s.search(testcase, 0))