class Solution(object):
    def hammingWeight(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        bit = 0
        while n >= 1:
            if n % 2 == 1:
               bit += 1
            n = n // 2
        return bit

n = 2147483645
res = Solution().hammingWeight(n)
print(res)
