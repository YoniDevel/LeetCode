class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n):
            if s == goal: return True
            s = s[1:n] + s[0]
        return False
