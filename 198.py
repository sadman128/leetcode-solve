class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2 = 0  # max profit two houses back
        prev1 = 0  # max profit from the last house

        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp

        return prev1

nums = [1,2,3,1]
res = Solution().rob(nums)
print(res)
