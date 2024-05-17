from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newList: List[int] = [];
        for i in range(n):
            newList.append(nums[i]);
            newList.append(nums[i + n]);
        return newList;
