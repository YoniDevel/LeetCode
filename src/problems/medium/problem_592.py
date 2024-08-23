import re
import math
from functools import reduce


class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall(r'(-?\d+)/(\d+)', expression)
        numerators = [int(num) for num, _ in fractions]
        denominators = [int(den) for _, den in fractions]
        lcm = reduce(math.lcm, denominators)
        result_numerator = 0
        for i in range(len(numerators)):
            result_numerator += numerators[i] * (lcm // denominators[i])
        if result_numerator == 0: return "0/1"
        result_gcd = reduce(math.gcd, [lcm, result_numerator])
        return f"{result_numerator // result_gcd}/{lcm // result_gcd}"
        