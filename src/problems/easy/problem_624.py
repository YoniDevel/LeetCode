from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_diff = 0
        for i in range(len(arrays)):
            small, big = arrays[i][0], arrays[i][-1]
            for j in range(i + 1, len(arrays)):
                diff_1 = arrays[j][-1] - small
                diff_2 = big - arrays[j][0]
                if diff_1 > max_diff:
                    max_diff = diff_1
                if diff_2 > max_diff:
                    max_diff = diff_2
        return max_diff
