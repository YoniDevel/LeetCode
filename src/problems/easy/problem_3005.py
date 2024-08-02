from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies_dict = {}
        for num in nums:
            if num not in frequencies_dict:
                frequencies_dict[num] = 1
            else:
                frequencies_dict[num] += 1
        frequencies = list(frequencies_dict.values())
        max_frequency = max(frequencies)
        return frequencies.count(max_frequency) * max_frequency
