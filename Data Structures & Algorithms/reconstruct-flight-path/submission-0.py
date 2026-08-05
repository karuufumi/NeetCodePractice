from collections import defaultdict
from heapq import heapify, heappop
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets):
            graph[src].append(dst)
        for dests in graph.values():
            heapify(dests)

        path = []
        def visit(airport: str) -> None:
            while graph[airport]:
                visit(heappop(graph[airport]))
            path.append(airport)

        visit("JFK")
        return path[::-1]