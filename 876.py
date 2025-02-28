
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        slowNode = head
        fastNode = head
        while fastNode and fastNode.next:
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        return slowNode


nums = [1,2,3,4,5,6]

head = ListNode(nums[0])
head.next = ListNode(nums[1])
head.next.next = ListNode(nums[2])
head.next.next.next = ListNode(nums[3])
head.next.next.next.next = ListNode(nums[4])
#head.next.next.next.next.next = ListNode(nums[5])

res = Solution().middleNode(head)
while res != None:
    print(res.val)
    res = res.next
