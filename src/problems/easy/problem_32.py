class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        for c in s:
            if c in t[p:]:
                while t[p] != c:
                    p += 1
                p += 1
            else:
                return False
        return True
