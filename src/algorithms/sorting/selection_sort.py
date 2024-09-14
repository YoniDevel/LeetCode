from typing import List

def selection_sort(lst: List[int]) -> None:
    n = len(lst)
    for i in range(n):
        m_index = i
        for j in range(i + 1, n):
            if lst[m_index] > lst[j]:
                m_index = j
        lst[i], lst[m_index] = lst[m_index], lst[i]
    return None
