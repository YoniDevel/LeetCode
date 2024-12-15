from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        connections = {}
        for edge in edges:
            for node in edge:
                if node in connections:
                    connections[node] += 1
                else:
                    connections[node] = 0
        for node in connections:
            if connections[node] == len(edges) - 1:
                return node