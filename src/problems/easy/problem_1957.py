class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        while (i < len(s) - 2):
            while i < len(s) - 2 and s[i] == s[i + 1] and s[i] == s[i + 2]:
                s = s[:i] + s[i + 1:]
            i += 1
        return s
            
print(Solution().makeFancyString('aaabaaaa'))
