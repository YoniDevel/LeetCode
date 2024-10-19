from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks_map = {}
        for i, num in enumerate(sorted(set(arr))):
            ranks_map[num] = i + 1
        return [ranks_map[num] for num in arr]
