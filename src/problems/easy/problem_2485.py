class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = [x for x in range(1, n + 1)]
        left_sum = 0
        right_sum = sum(nums)
        for num in nums:
            left_sum += num
            right_sum -= num - 1
            if left_sum == right_sum:
                return num
        return -1
