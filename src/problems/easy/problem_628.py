from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return max(sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3], sorted_nums[0] * sorted_nums[1] * sorted_nums[-1])
