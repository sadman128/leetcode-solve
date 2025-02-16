class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        mid = 0
        while left <= right :
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

nums = [-1,0,3,5,9,12]
target = 3

res = Solution().search(nums, target)
print(res)
