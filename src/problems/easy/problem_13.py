class Solution:
    def romanToInt(self, s: str) -> int: # runs in 39 ms
        romanDict: dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        potentialRomanArray: list[str] = ['I', 'X', 'C']
        specialRomanDict: dict = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        sum: int = 0 
        i: int = 0
        
        while (i < len(s)):
            if s[i] in potentialRomanArray:
                withNext = s[i] + s[i + 1] if i < len(s) - 1 else s[i]
                if withNext in specialRomanDict:
                    sum += specialRomanDict[withNext]
                    i += 2
                    continue
            sum += romanDict[s[i]]
            i += 1
        return sum
            
            
        
        
