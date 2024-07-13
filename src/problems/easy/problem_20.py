class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_dict = { ')': '(', '}': '{', ']': '[' }
        openning_set = set(closing_dict.values())

        
        for char in s:
            print(char)
            if char in openning_set:
                stack.append(char)
            else:
                if not stack or stack[-1] != closing_dict[char]:
                    return False
                stack.pop()
        return stack == []
    