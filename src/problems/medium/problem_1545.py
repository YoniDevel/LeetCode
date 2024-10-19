class Solution:
    def invert(self, bin_num: str) -> str:
        return "".join(list(map(lambda c: '0' if c == '1' else '1', bin_num)))
    
    def findKthBit(self, n: int, k: int) -> str:
        sequence = ['0']
        for i in range(n - 1):
            sequence.append("%s1%s" % (sequence[i], self.invert(sequence[i])[::-1]))
        return sequence[-1][k - 1]
