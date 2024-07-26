from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        i = 0
        while i < len(nums) - 1:
            if sorted_nums[i] != sorted_nums[i + 1]:
                return sorted_nums[i]
            i += 2
        return sorted_nums[i]
    
            