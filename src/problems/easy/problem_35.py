from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_pointer = 0;
        right_pointer = len(nums) - 1;
        if (target < nums[left_pointer]): return left_pointer;
        if (target > nums[right_pointer]): return right_pointer + 1;

        while True:
            if (target > nums[right_pointer]): return right_pointer + 1;
            if (target == nums[right_pointer]): return right_pointer;
            if (target <= nums[left_pointer]): return left_pointer;
            left_pointer += 1;
            right_pointer -= 1;
    def betterSearchInsert(self, nums: list[int], target: int) -> int:
        left_pointer, right_pointer = 0, len(nums) - 1;
        while left_pointer <= right_pointer:
            pivot = (left_pointer + right_pointer) // 2;
            if nums[pivot] == target:
                return pivot;
            if target < nums[pivot]:
                right_pointer = pivot - 1;
            else:
                left_pointer = pivot + 1;
        return left_pointer;