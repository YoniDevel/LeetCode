from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newList: list[int] = [nums[0]];
        for i in range(1,  len(nums)):
            if nums[i] is not nums[i - 1]:
                newList.append(nums[i]);
        nums = newList;
        return len(nums);
    
sol = Solution();
print(sol.removeDuplicates([1, 1, 2]));
