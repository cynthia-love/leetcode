# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法4, 方法3的代码精简版
    精简点在于, 不足k的部分, 再翻回去, 可以在下一个递归做尾插
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if not head: return head

        ans, h, c = ListNode(-1), head, 1

        while h and c <= k: h.next, ans.next, h, c = ans.next, h, h.next, c + 1

        if c > k: head.next = self.reverseKGroup(h, k)
        else: ans.next = self.reverseKGroup(ans.next, c - 1)

        return ans.next


x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(3)
x.next.next.next = ListNode(4)
x.next.next.next.next = ListNode(5)
s = Solution()
a = s.reverseKGroup(x, 3)
while a:
    print(a.val, end=" ")
    a = a.next
print()


