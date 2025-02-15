class Solution(object):
    def myAtoi(self, s):
        minus = 0
        minusTrack = 0
        str = ""
        s = s.strip(" ")
        for c in range(0, len(s)):
            if s[c] == "-":
                if c<len(s)-1 and s[c+1].isdigit() and len(str) == 0:
                    if minusTrack == 1:
                        break
                    minus = 1
                    continue
                else:
                    break

            if s[c] == "+":
                if c<len(s)-1 and s[c+1].isdigit() and len(str) == 0:
                    continue
                else:
                    break
            if s[c] == "0":
                str = str + "0"
                minusTrack = 1
            elif s[c] == "1":
                str = str + "1"
                minusTrack = 1
            elif s[c] == "2":
                str = str + "2"
                minusTrack = 1
            elif s[c] == "3":
                str = str + "3"
                minusTrack = 1
            elif s[c] == "4":
                str = str + "4"
                minusTrack = 1
            elif s[c] == "5":
                str = str + "5"
                minusTrack = 1
            elif s[c] == "6":
                str = str + "6"
                minusTrack = 1
            elif s[c] == "7":
                str = str + "7"
                minusTrack = 1
            elif s[c] == "8":
                str = str + "8"
                minusTrack = 1
            elif s[c] == "9":
                str = str + "9"
                minusTrack = 1
            else:
                break
        if str == "":
            return 0
        val = int(str)
        if minus == 0:
            if val > 2147483647:
                return 2147483647
            return val
        else:
            val = -1 * val
            if val < -2147483648:
                return -2147483648
            return val

s = "   +0 123"
res = Solution().myAtoi(s)
print(res)
