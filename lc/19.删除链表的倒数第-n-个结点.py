#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(next=head)
        p, q = dummy, dummy
        for _ in range(n + 1):
            q = q.next
        while q:
            p, q = p.next, q.next
        p.next = p.next.next
        return dummy.next
        
# @lc code=end

