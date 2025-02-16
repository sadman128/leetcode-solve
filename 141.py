class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        lst = []
        while head.next is not None :
            if head in lst:
                return True
            lst.append(head)
            head = head.next

        return False

head = [1,2]
node = ListNode(head[0])
node.next = ListNode(head[1])

res = Solution().hasCycle(node)
print(res)
