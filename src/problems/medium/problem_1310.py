from typing import List, Dict, Optional

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(len(arr) - 1):
            arr[i + 1] ^= arr[i]
        return [arr[j] ^ arr[i - 1] if i else arr[j] for i, j in queries]
    
    def xor_array(self, arr: List[int]) -> int:
        current_xor = arr[0]
        for i in range(1, len(arr)):
            current_xor ^= arr[i]
        return current_xor
    
    def is_query_cotaining_other(self, query_1: List[int], query_2: List[int]) -> bool:
        return query_1[0] == query_2[0] and query_1[1] > query_2[1]
    
    def extract_contained_processed_queries(self, query: List[int], processed_queries: dict) -> int:
        result = (query[0], query[0])
        for processed_query in processed_queries:
            if self.is_query_cotaining_other(query, processed_query) and processed_query[1] > result[1]:
                result = processed_query
        return -1 if result == (query[0], query[0]) else processed_queries[result]
                
    def xorQueries2(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        processed_queries = {}
        for query in queries:
            result = 0
            if (query[0], query[1]) in processed_queries:
                answer.append(processed_queries[(query[0], query[1])])
            else:
                contained_query_result = self.extract_contained_processed_queries(query, processed_queries)
                if contained_query_result != -1:
                    result = self.xor_array([contained_query_result, *arr[query[0] + 1: query[1] + 1]])
                result = self.xor_array(arr[query[0]: query[1] + 1])
                answer.append(result)
                processed_queries[(query[0], query[1])] = result
        return answer

    def xor(self, left: int, right: int) -> int:
        if left == right: return left
        result = ''
        left_bin, right_bin = bin(left)[2:], bin(right)[2:]
        len_left, len_right = len(left_bin), len(right_bin)
        bigger_length = max(len_left, len_right)
        
        if len_left == bigger_length: 
            right_bin = right_bin.zfill(bigger_length)
        else:
            left_bin = left_bin.zfill(bigger_length)

        for i in range(bigger_length):
            if right_bin[i] == left_bin[i]:
                result += '0'
            else:
                result += '1'
        return int(result, 2)
    
print(Solution().xor(3, 4))