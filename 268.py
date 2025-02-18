class Solution(object):
    def missingNumber(self, nums):
        max = nums[0]
        min = nums[0]
        for i in nums:
            if i > max:
                max = i
            if i < min:
                min = i
        if min != 0:
            return 0
        if max != len(nums):
            return len(nums)

        dic = {}
        for i in range (min,max+1):
            dic[i] = 0
        for i in nums:
            dic[i] += 1
        for i in dic:
            if dic[i] == 0:
                return i
        return max+1



nums = [0,1]
res = Solution().missingNumber(nums)
print(res)
