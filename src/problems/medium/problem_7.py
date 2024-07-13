class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if x < 0:
            sign = -1
            x = -x
        else: sign = 1
        reversed_num = int(str(x)[::-1])
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        return reversed_num * sign
 