class Solution(object):
    def singleNumber(self, nums):
        val = nums[0]
        for num in nums[1:]:
            val = val^num
        return val


nums = [4,1,2,1,2]
res = Solution().singleNumber(nums)
print(res)
