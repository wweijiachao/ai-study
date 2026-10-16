#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        cur_level = [root]
        res = []
        while cur_level:
            next_level = []
            level_res = []
            for node in cur_level:
                level_res.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if len(level_res) > 0:
                res.append(level_res)
            cur_level = next_level
        return res


        
        
# @lc code=end