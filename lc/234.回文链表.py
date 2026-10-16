#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 先找到后半段链表的开始，同时将前半段链表反转
        # 然后对照两个链表部分
        if not head.next:
            return True
        slow = fast = head
        pre = None
        while fast:
            if not fast.next:
                # 奇数个节点，此时slow是两个半串的公共起点，
                # 从前后两个节点判断即可
                slow = slow.next
                break
            else:
                fast = fast.next.next
                # 慢节点前进一步的同时反转
                nxt = slow.next
                slow.next = pre
                pre, slow = slow, nxt
        # 循环退出代表快节点已经走完链表，此时pre是前半的最后一个节点
        p, q = pre, slow
        while q:
            if p.val != q.val:
                return False
            p, q = p.next, q.next
        return True
        
# @lc code=end
