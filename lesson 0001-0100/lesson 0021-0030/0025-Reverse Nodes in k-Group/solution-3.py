# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 试试始终翻转, 不够k再翻回去, 在当前递归再做一次尾插
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def rf(head=head):
            # 1->2->3->4; ->-1
            if not head: return head
            ans, h, c = ListNode(-1), head, 1

            while h and c <= k:
                h.next, ans.next, h, c = ans.next, h, h.next, c+1
            # 以k=3为例, 循环退出后, h指向4, c=4; 第二次递归, None, 2
            # 情况1, 不够k个, 翻回去, -1->2->1
            if c-1 < k:
                # 这里的ans.next=None是必不可少的
                h, ans.next = ans.next, None
                while h:
                    h.next, ans.next, h = ans.next, h, h.next
            else:
                # 够了, 要进入下一个递归, 此时head指向1, h指向4
                head.next = rf(h)

            return ans.next

        return rf()


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


