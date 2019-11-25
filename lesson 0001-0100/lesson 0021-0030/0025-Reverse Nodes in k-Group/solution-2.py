# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 外层递归, 每k的翻转用尾插
    比如1->2->3, ans->1, ans->2->1, ans->3->2->1
    注意, 不足k个的不翻转, 所以这里得先遍历一次计算长度
    (方法1不一样, 怎么都得遍历一次插入元素的)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def rf(h=head):

            if not h: return h

            r, c = h, 1

            while r.next and c < k:
                r, c = r.next, c+1

            if c < k: return h

            # 满足长度为k, 进行翻转, 此时h和r分别指向首尾
            # remains保存剩余部分用于递归
            ans, l, remains = ListNode(-1), h, r.next

            # ->-1->1, 插入个->2->3, 这里要分析好怎么写
            while l is not remains:
                # 这里需要好好研究一下python的赋值特性
                """
                    a=b=c=1, 这种, 先a=1, 然后把a赋值给b和c(暂时没遇到理解错误带来的坑)
                    a, b = a+1, a+3, 这种, 加载a,算a+1, 加载a,算a+1, 假如a=3, 则结果为46
                    l.next, ans.next, l = ans.next, l, l.next, 右边没毛病, 拿到三个
                    指针, 分别指向1, 2, 3, 但是拆包的时候是有顺序的, 左边三个是依次赋值
                    
                """
                # l.next要指向1, ans.next要指向2, l然后指向3
                # 因为拆包的时候是按顺序来的, 所以要注意先赋值的对后赋值的影响
                # 这里比较明显的是l不能在l.next前面, 那么以下几种写法应该都可以:
                """
                    l.next, ans.next, l = ans.next, l, l.next
                    ans.next, l.next, l = l, ans.next, l.next
                    l.next, l, ans.next = ans.next, l.next, l
                """
                l.next, ans.next, l = ans.next, l, l.next

            h.next = rf(remains)
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

a = [0, 0, 0, 0]
i, a[i], i, a[i] = (0, 1, 2, 3)
import dis
print(dis.dis("a=b=c=1"))
print(dis.dis("a, b = a+1, a+3"))
print(dis.dis("l.next, ans.next, l = ans.next, l, l.next"))