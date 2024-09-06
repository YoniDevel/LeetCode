class Solution:
    def digit_sum(self, n: int) -> int:
        return sum([int(digit) for digit in str(n)])    
    
    def get_letter_value(self, letter: str) -> str:
        return str(ord(letter) - 96)
    
    def getLucky(self, s: str, k: int) -> int:
        converted_s = int(''.join(map(self.get_letter_value, s)))
        for _ in range(k):
            converted_s = self.digit_sum(converted_s)
        return converted_s
