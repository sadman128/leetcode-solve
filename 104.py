class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

class Solution(object):
    def maxDepth(self, root):

        count = 0

        def depth(root, cnt):
            if root is None:
                return cnt
            cnt += 1
            return max(depth(root.left, cnt), depth(root.right, cnt))
        return depth(root, count)

root = [3,9,20,None,None,15,7]

head = TreeNode(root[0])
head.left = TreeNode(root[1])
head.right = TreeNode(root[2])
head.right.left = TreeNode(root[5])
head.right.right = TreeNode(root[6])



res = Solution().maxDepth(head)
print(res)

