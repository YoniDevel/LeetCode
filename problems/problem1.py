from typing import List, Dict;

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # O(n^2) complexity
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j];
                
    def BetterTwoSum(self, nums: List[int], target: int) -> List[int]: # O(n) complexity with dictionary
        numsDict: Dict = {};
        n: int = len(nums);

        for i in range(n):
            numsDict[nums[i]] = i;

        {3: 0, 2: 1, 4: 2}

        for i in range(n):
            difference = target - nums[i];
            if difference in numsDict and numsDict[difference] != i:
                return [i, numsDict[difference]];
