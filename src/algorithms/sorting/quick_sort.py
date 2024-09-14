import random
from typing import List

def quick_sort(lst: List[int]) -> List[int]:
    """ quick sort of lst """
    if len(lst) <= 1: 
        return lst
    else:
        pivot = random.choice(lst) # select a random element from list
        #pivot = lst[0] #for a deterministic quicksort
        
        smaller = [elem for elem in lst if elem < pivot] 
        equal   = [elem for elem in lst if elem == pivot]      
        greater = [elem for elem in lst if elem > pivot]

        return quick_sort(smaller) + equal + quick_sort(greater)
