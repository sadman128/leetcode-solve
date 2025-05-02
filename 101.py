class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):

        if not root:
            return True
        if not root.left and not root.right:
            return True

        if not root.left or not root.right:
            return False

        leftqueue = [root.left]
        rightqueue = [root.right]

        while leftqueue and rightqueue:

            left = leftqueue.pop(0)
            right = rightqueue.pop(0)

            if left and right:

                if left.val == right.val:

                    leftqueue.append(left.left)
                    leftqueue.append(left.right)

                    rightqueue.append(right.right)
                    rightqueue.append(right.left)

                    continue

                else:
                    return False

            elif not left == right:
                return False

        return True


# Hardcoded tree from [1, 2, 2, null, 3, null, 3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)

x = Solution().isSymmetric(root)
print(x)


