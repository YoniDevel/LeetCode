from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_for_calc = sum(nums[:k])
        max_average = sum_for_calc / k
        for i in range(k, len(nums)):
            sum_for_calc -= nums[i - k]
            sum_for_calc += nums[i]
            average = sum_for_calc / k
            if average > max_average:
                max_average = average
        return max_average
