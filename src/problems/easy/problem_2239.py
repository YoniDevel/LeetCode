from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_dist, min_dist_elem = abs(nums[0]), nums[0]
        for num in nums[1:]:
            if (abs(num) < min_dist) or (abs(num) == min_dist and num > min_dist_elem):
                min_dist, min_dist_elem = abs(num), num
        return min_dist_elem
