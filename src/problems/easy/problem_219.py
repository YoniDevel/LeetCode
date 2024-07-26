from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices_dict = {}
        for i in range(len(nums)):
            if nums[i] not in indices_dict:
                indices_dict[nums[i]] = i
            else:
              if i - indices_dict[nums[i]] <= k:
                  return True
              else: 
                  indices_dict[nums[i]] = i
        return False  
          