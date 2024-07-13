class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        indicator = -1
        n1, n2 = len(haystack), len(needle)
        if n2 > n1: return indicator
        for i in range((n1 - n2) + 1):
            if haystack[i: i + n2] == needle:
                indicator = i
                break
        return indicator
    