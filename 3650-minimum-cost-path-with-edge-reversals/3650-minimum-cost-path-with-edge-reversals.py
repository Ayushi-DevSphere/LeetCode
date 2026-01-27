import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))
        
        pq = [(0, 0)]
        dist = [float('inf')] * n
        dist[0] = 0
        
        while pq:
            current_cost, u = heapq.heappop(pq)
            
            if current_cost > dist[u]:
                continue
            
            if u == n - 1:
                return current_cost
            
            for v, weight in graph[u]:
                new_cost = current_cost + weight
                
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
        
        return -1 if dist[n - 1] == float('inf') else dist[n - 1]
