class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, l, r):

        if not l and not r:
            return True

        if not l or not r:
            return False

        leftqueue = [l]
        rightqueue = [r]

        while leftqueue and rightqueue:

            left = leftqueue.pop(0)
            right = rightqueue.pop(0)

            if left and right:

                if left.val == right.val:

                    leftqueue.append(left.left)
                    leftqueue.append(left.right)
                    rightqueue.append(right.left)
                    rightqueue.append(right.right)

                    continue

                else:
                    return False

            elif not left == right:
                return False

        return True



