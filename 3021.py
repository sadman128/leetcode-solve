class Solution(object):
    def flowerGame(self, n, m):
        pass
        cnt = 0
        nEven = 0
        nOdd = 0
        mEven = 0
        mOdd = 0
        if n % 2 == 0:
            nEven = nOdd = n // 2
        else:
            nEven = (n-1) // 2
            nOdd = n - nEven

        if m % 2 == 0:
            mEven = mOdd = m // 2
        else:
            mEven = (m-1) // 2
            mOdd = m - mEven

        return nEven*mOdd + mEven*nOdd



n = 1
m = 5
res = Solution().flowerGame(n, m)
print(res)
