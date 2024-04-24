from typing import List


class Solution:
    def findShortestString(self, strs: List[str]) -> str:
        minLength: int = len(strs[0]);
        minString: str = strs[0];
        
        for s in strs[1::]:
            length = len(s);
            if (length < minLength):
                minLength = length;
                minString = s;
        return minString;
    
    def longestCommonPrefix(self, strs: List[str]) -> str | None:
        shortestString: str = self.findShortestString(strs);
        booli: bool = False;
        for i in range(len(shortestString), 0, -1):
            for s in strs:
                if not s.startswith(shortestString[0:i]):
                    booli = False;
                    break;
                booli = True;
            if booli:
                return shortestString[0:i];
        if not booli:
            return "";