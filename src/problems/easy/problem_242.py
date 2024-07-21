class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_set = set(s)
        m = {}
        for char in s:
            if char not in set(m.keys()):
                m[char] = 1
            else: 
                m[char] += 1
        for char in t:
            if (char not in chars_set):
                return False
            m[char] -= 1
        for value in m.values():
            if value != 0:
                return False
        return True
