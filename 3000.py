import math

class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        diag = []
        for i in range(len(dimensions)):
            d = dimensions[i][0] ** 2 + dimensions[i][1] ** 2
            d = math.sqrt(d)
            diag.append(d)
        mxd = max(diag)
        idx = []
        for i in range(len(diag)):
            if diag[i] >= mxd:
                idx.append(i)

        if len(idx) == 1:
            return dimensions[idx[0]][0] * dimensions[idx[0]][1]
        else:
            new = []
            for i in range(len(idx)):
                new.append(dimensions[idx[i]][0] * dimensions[idx[i]][1])

            return max(new)







dimensions = [[3,4],[4,3]]
res = Solution().areaOfMaxDiagonal(dimensions)
print(res)
