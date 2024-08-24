import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c ** 0.5)
        while (left <= right):
            squares_sum = left ** 2 + right ** 2
            if squares_sum == c: return True
            if squares_sum < c:
                left += 1
            elif squares_sum > c:
                right -= 1
        return False
