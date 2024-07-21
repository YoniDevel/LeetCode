from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        start_index = 0
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                if i - start_index > n / 2:
                    return nums[i - 1]
                start_index = i
        return nums[-1]
      
          