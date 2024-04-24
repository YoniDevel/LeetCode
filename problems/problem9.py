class Solution:
    def isPalindrome(self, x: int) -> bool: # with conversion to a string
        return str(x) == str(x)[::-1];
    def isPalindromeWithoutString(self, x: int) -> bool: # without converting to a string, comp. O(n)
        if x < 10:
            if x < 0:
                return False;
            return True;
        
        temp: int = x;
        reversedNum: int = 0;
        
        while (temp != 0):
            reversedNum *= 10;
            reversedNum += temp % 10;
            temp //= 10;
        return reversedNum == x;
