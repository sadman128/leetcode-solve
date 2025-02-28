class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        def divide(left, right, node):
            if left>right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = divide(left, mid - 1, node.left)
            node.right = divide(mid + 1, right, node.right)
            return node

        node = TreeNode(0)
        left = 0
        right = len(nums) - 1
        node = divide(left, right, node)
        return node


nums = [-10,-3,0,5,9]

res = Solution().sortedArrayToBST(nums)

def printTree(root):
    if root is None:
        return
    printTree(root.left)
    print(root.val)
    printTree(root.right)

printTree(res)
