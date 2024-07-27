class Solution:
    
    def climbStairs(self, n: int) -> int:
        calculations_dict = {}
        return self.helper(n, calculations_dict)

    def helper(self, n: int, calculations_dict: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in calculations_dict:
            calculations_dict[n] = self.helper(n-1, calculations_dict) + self.helper(n-2, calculations_dict)
        return calculations_dict[n]
