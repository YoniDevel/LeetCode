# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val:int=0, next=None):
        self.val = val
        self.next = next
        
    def toString(self):
        stringList: str = ""
        p: Optional[ListNode] = self
        while (p != None):
            stringList += str(p.val) + "->"
            p = p.next
        return stringList
class Solution:
    def getLength(self, l: Optional[ListNode]) -> int:
        p: Optional[ListNode] = l
        length: int = 0
        while(p != None):
            length += 1
            p = p.next
        return length
    def getListsByLength(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        length1: int = self.getLength(l1)
        length2: int = self.getLength(l2)
        if length1 >= length2:
            return [l1, l2, length1 - length2]
        return [l2, l1, length2 - length1]
    def addZeros(self, l: Optional[ListNode], n: int):
        p = l
        while (p.next != None and p != None): # type: ignore
            p = p.next
        for i in range(n):
            p.next = ListNode() # type: ignore
            p = p.next # type: ignore
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode: 
        [longer, shorter, n] = self.getListsByLength(l1, l2)
        self.addZeros(shorter, n)
        result: ListNode = ListNode()
        
        pShorter = shorter
        pLonger = longer
        pResult = result
        
        remainder: int = 0
        sum: int = 0
        
        while(pShorter != None and pLonger != None and pResult != None):
            sum = pShorter.val + pLonger.val + remainder
            if (sum >= 10):
                pResult.val = sum % 10
                remainder = 1
            else: 
                pResult.val = sum
                remainder = 0 
            if (pShorter.next != None):
                pResult.next = ListNode()
                pResult = pResult.next
            pShorter = pShorter.next
            pLonger = pLonger.next
        if remainder != 0: pResult.next = ListNode(remainder)
        return result
