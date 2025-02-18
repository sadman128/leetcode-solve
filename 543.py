class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        lst = []
        def dfs(root):
            if not root:
                lst.append(0)
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            lst.append(left + right)
            return 1 + max(left, right)
        value = dfs(root.left) + dfs(root.right)
        lst.append(value)
        return max(lst)

num = [1,2,3,4,5]
root = TreeNode(num[0])
root.left = TreeNode(num[1])
root.right = TreeNode(num[2])
root.left.left = TreeNode(num[3])
root.left.right = TreeNode(num[4])

res = Solution().diameterOfBinaryTree(root)
print(res)
