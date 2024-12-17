from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_val = min(nums)
            for i in range(len(nums)):
                if nums[i] == min_val:
                    nums[i] *= multiplier
                    break
        return nums
