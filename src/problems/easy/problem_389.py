class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_ord, t_ord = sum([ord(c) for c in s]), sum([ord(c) for c in t])
        return chr(t_ord - s_ord)
