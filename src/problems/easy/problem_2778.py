from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s, length = 0, len(nums)
        for i in range(1, int(length ** 0.5) + 1):
            if length % i == 0:
                s += nums[i - 1] ** 2
                if length // i != i:
                    s += nums[(length // i) - 1] ** 2
        return s
