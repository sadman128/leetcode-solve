class Solution(object):
    def climbStairs(self, n):
        if n==1 : return 1
        if n==2 : return 2

        one = 1
        two = 2
        for i in range(2,n):
            curr = one + two
            one = two
            two = curr

        return two



n = 3
x = Solution().climbStairs(n)
print(x)
