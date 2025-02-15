class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dic1 = {str : int}
        dic2 = {str : int}
        for char in s:
            if char in dic1:
                dic1[char] = dic1[char] + 1
            else:
                dic1[char] = 1
        for char in t:
            if char in dic2:
                dic2[char] = dic2[char] + 1
            else:
                dic2[char] = 1
        return dic1 == dic2


s = "anagram"
t = "nagaram"
res = Solution().isAnagram(s, t)
print(res)
