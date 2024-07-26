class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squared_digits(n):
            return sum(int(digit) ** 2 for digit in str(n))
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_squared_digits(n)
        
        return n == 1