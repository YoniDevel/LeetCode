from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        state = 'undecided'
        max_length = 1
        current_length = 0
        for i in range(1, len(nums)):
            if state == 'inc':
                if nums[i] < nums[i - 1]:
                    max_length  = max([max_length, current_length])
                    state = 'dec'
                    current_length = 2
                elif nums[i] == nums[i - 1]:
                    max_length  = max([max_length, current_length])
                    state = "undecided"
                else:
                    current_length += 1
            elif state == 'dec':
                if nums[i] > nums[i - 1]:
                    max_length  = max([max_length, current_length])
                    state = 'inc'
                    current_length = 2
                elif nums[i] == nums[i - 1]:
                    max_length  = max([max_length, current_length])
                    state = "undecided"
                else:
                    current_length += 1
            else:
                if nums[i] > nums[i - 1]:
                    state = 'inc'
                    current_length = 2
                elif nums[i] < nums[i - 1]:
                    state = 'dec'
                    current_length = 2
        return max(max_length, current_length)
