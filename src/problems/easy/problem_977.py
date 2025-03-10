from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        L, R = 0, len(nums) - 1
        while L <= R:
            abs_L, abs_R = abs(nums[L]), abs(nums[R])
            if abs_L > abs_R:
                result.append(abs_L ** 2)
                L += 1
            else:
                result.append(abs_R ** 2)
                R -= 1
        return result[::-1]
