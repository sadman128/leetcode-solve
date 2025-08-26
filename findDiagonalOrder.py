class Solution(object):
    def findDiagonalOrder(self, mat):
        result = []
        if not mat or not mat[0]:
            return result

        m = len(mat) # row
        n = len(mat[0]) # col
        r , c = 0, 0
        s = 0
        while r < m and c < n:
            i = r
            j = c
            res = []

            while -1 < i < m and - 1 < j < n:

                res.append(mat[i][j])
                i = i - 1
                j = j + 1

            if s == 0:
                result = result + res
                s = 1
            else:
                result = result + res[::-1]
                s = 0
            r = r + 1
            if not r < m :
                c = c + 1
                r = r - 1

        return result


mat = [[2,3]]
res = Solution().findDiagonalOrder(mat)
print(res)

# 00 01 10 20 11 02
