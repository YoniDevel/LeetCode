from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        returned_list = []
        for num in nums:
            returned_list.append(sorted_nums.index(num))
        return returned_list
       