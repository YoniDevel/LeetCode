class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x == 1: return 1
        left_pointer, right_pointer = 0, x - 1
        while left_pointer <= right_pointer:
            middle = (right_pointer + left_pointer) // 2
            squared = middle * middle
            if x == squared:
                return middle
            elif x > squared:
                left_pointer = middle + 1
            else:
                right_pointer = middle - 1
        return right_pointer
