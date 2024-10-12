from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        frequencies_map = {}
        frequent_num, max_frequency = 10 ** 5, 0
        for num in nums:
            if num % 2 == 0:
                if num not in frequencies_map:
                    frequencies_map[num] = 1
                else:
                    frequencies_map[num] += 1
                if frequencies_map[num] > max_frequency or frequencies_map[num] == max_frequency and num < frequent_num:
                    frequent_num, max_frequency = num, frequencies_map[num]
        return -1 if max_frequency == 0 else frequent_num
            