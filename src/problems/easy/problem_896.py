from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        status = "undecided"
        while len(nums) > 2 and nums[0] == nums[1]:
            nums.pop(0)
        if len(nums) == 1: return True
        status = "inc" if nums[1] > nums[0] else "dec"
        for i in range(1, len(nums)):
            if (nums[i] > nums[i - 1] and status == "dec") or (nums[i] < nums[i - 1] and status == "inc"):
                return False
        return True
