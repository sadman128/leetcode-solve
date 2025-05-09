class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):

        def dfs(node, value):
            if not node:
                return
            dfs(node.left, value)
            value.append(node.val)
            dfs(node.right, value)

        def is_sorted(nums):
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]: 
                    return False
            return True

        value = []
        dfs(root, value)
        return is_sorted(value)


root = TreeNode(0)
#root.left = TreeNode(1)
root.right = TreeNode(-1)

print(Solution().isValidBST(root))
