from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a1, a2 = s1.split(" "), s2.split(" ")
        return [word for word in list(set(a1).symmetric_difference(set(a2))) if (a1 + a2).count(word) == 1]
