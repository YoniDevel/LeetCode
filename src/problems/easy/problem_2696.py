class Solution:
    def minLength(self, s: str) -> int:
        while s.find('AB') + s.find('CD') != -2:
            s = s.replace('AB', '').replace('CD', '')
        return len(s)
