# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析, 链表两两互换, 不能直接换值
    比如1->2->3->4, 变成2->1->4->3
    思路, 双指针p, q
    0->1->2->3->4, 两者指向变化如下:
    (捋不明白就拿临时变量全记下来)
    0, 2, p.next, p.next.next, p.next.next.next = q, p.next, q.next
"""
"""
    方法1, 双指针
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def pl(self, head: ListNode):
        while head:
            print(head.val, end=" ")
            head = head.next
        print("")

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        ans = ListNode(-1)
        ans.next = head

        p, q = ans, head.next

        while True:
            # 全存了, 没必要为了简洁把脑子绕进去, -1->1->2->3
            x, y, z = p.next, q, q.next
            p.next, p.next.next, p.next.next.next = y, x, z

            # 这里终止条件要考虑奇数和偶数情况
            if not z or not z.next:
                return ans.next
            else:
                p, q = x, z.next


x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(3)
x.next.next.next = ListNode(4)
s = Solution()
a = s.swapPairs(x)
while a:
    print(a.val, end=" ")
    a = a.next
