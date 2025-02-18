class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if dic.get(num):
                dic[num] += 1
            else:
                dic[num] = 1
        max = nums[0]
        for i in dic:
            if dic[i] > dic[max]:
                max = i
        return max

nums = [2,2,1,1,1,2,2]
res = Solution().majorityElement(nums)
print(res)
