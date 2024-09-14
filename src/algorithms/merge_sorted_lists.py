from typing import List

def merge(A: List[int], B: List[int]) -> List[int]:
    """ merging two lists into a sorted list
        A and B must be sorted! """
    n = len(A)
    m = len(B)
    C = [0 for _ in range(n + m)]

    a=0; b=0; c=0
    while  a < n  and  b < m:
        if A[a] < B[b]:
            C[c] = A[a]
            a+=1
        else:
            C[c] = B[b]
            b+=1
        c+=1

    if a == n: #A was completed
        while b < m:
            C[c] = B[b]
            b+=1
            c+=1
    else: #B was completed
        while a < n:
            C[c] = A[a]
            a+=1
            c+=1
        
    return C