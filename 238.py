class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        left = []
        right = []
        for i in range(n):
            left.append(1)
            right.append(1)

        for i in range(1, n):
            left[i] = left[i-1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i+1] * nums[i + 1]
            left[i] = left[i] * right[i]

        return left



nums = [-1,1,0,-3,3]
arr = Solution().productExceptSelf(nums)
print(arr)
