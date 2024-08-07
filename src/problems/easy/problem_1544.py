class Solution:
    def makeGood(self, s: str) -> str:
        while True:
            starting_length = len(s)
            for i in range(starting_length - 1):
                if ((s[i].isupper() and s[i + 1] == s[i].lower()) or (s[i].islower() and s[i + 1] == s[i].upper())):
                    s = f'{s[0:i]}{s[i + 2:]}'
                    break
            if len(s) == starting_length or len(s) <= 1: break
        return s