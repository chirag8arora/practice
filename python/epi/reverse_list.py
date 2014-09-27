# merge sorted list
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

    def __iter__(self):
        while self:
            yield self
            self = self.next

class ListFactory():
    def gen_list(self, A):
        if not A:
            return None
        dummy_head = ListNode(0)
        node = dummy_head
        for i in A:
            node.next = ListNode(i)
            node = node.next
        return dummy_head.next

class Solution():
    def reverseIter(self, head):
        if not head:
            return
        p1 = head
        p2 = head.next
        while p1 and p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        head.next = None
        return p1


        # 1->2->3 tmp=3,p2=2,p1=2 -> p1 = 2, p2 = 3
        # 1-><-2<-3
    def reverse(self, head):
        return self.recursionHelper(head)[0]

    def recursionHelper(self, head):
        if not head:
            return None, None
        if not head.next:
            return head, head
        if head.next:
            nh, nt = self.recursionHelper(head.next)
            nt.next = head
            head.next = None
            t = head
            h = nh
            return h, t




f = ListFactory()
l1 = f.gen_list([1,4,7,2,3,6])
s = Solution()
for i in s.reverseIter(l1):
    print i.val
# 1 nh = none, nt = none
#  6->4 -> 1
