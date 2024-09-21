class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l = len(s)
        if l != len(t): return False
        s_to_t_mappings = {}
        for i in range(l):
            if s[i] not in s_to_t_mappings:
                if t[i] in s_to_t_mappings.values():
                    return False
                s_to_t_mappings[s[i]] = t[i]
            elif s_to_t_mappings[s[i]] != t[i]:
                return False
        return True
