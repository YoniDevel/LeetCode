class Solution:
    def findComplement(self, num: int) -> int:
        return int("".join(list(map(lambda c: '1' if c == '0' else '0', bin(num)[2:]))), 2)
