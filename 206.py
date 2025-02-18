class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        node = ListNode(0)
        root = node
        return self.reverse(head, node).next

    def reverse(self, head, node):
        if head.next != None:
            node = self.reverse(head.next, node)
        root = node
        while root.next:
            root = root.next
        root.next = ListNode(head.val)
        return node


head = [1,2,3,4,5]
node = ListNode(head[0])
node.next = ListNode(head[1])
node.next.next = ListNode(head[2])
node.next.next.next = ListNode(head[3])
node.next.next.next.next = ListNode(head[4])
res = Solution().reverseList(node)


while res:
    print(res.val)
    res = res.next
