from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right_pointer, left_pointer = len(nums) - 1, 0
        while (left_pointer <= right_pointer):
            middle = (left_pointer + right_pointer) // 2
            if (nums[middle] == target):
                return middle
            elif nums[middle] > target:
                right_pointer = middle - 1
            else:
                left_pointer = middle + 1
        return -1