from typing import List
from functools import cache

class Node:
    def __init__(self):
        self.children = [None] * 26
        self.v = -1

class Solution:
    def minimumCost(self, source: str, target: str, 
                    original: List[str], changed: List[str], 
                    cost: List[int]) -> int:
        m = len(cost)
        g = [[float('inf')] * (m << 1) for _ in range(m << 1)]
        for i in range(m << 1):
            g[i][i] = 0
        
        root = Node()
        idx = 0
        
        def insert(w: str) -> int:
            nonlocal idx
            node = root
            for c in w:
                i = ord(c) - ord("a")
                if node.children[i] is None:
                    node.children[i] = Node()
                node = node.children[i]
            if node.v < 0:
                node.v = idx
                idx += 1
            return node.v
        
        # Build cost graph
        for x, y, z in zip(original, changed, cost):
            x = insert(x)
            y = insert(y)
            g[x][y] = min(g[x][y], z)
        
        # Floyd-Warshall
        for k in range(idx):
            for i in range(idx):
                if g[i][k] >= float('inf'):
                    continue
                for j in range(idx):
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        
        @cache
        def dfs(i: int) -> int:
            if i >= len(source):
                return 0
            res = dfs(i + 1) if source[i] == target[i] else float('inf')
            p = q = root
            for j in range(i, len(source)):
                p = p.children[ord(source[j]) - ord("a")]
                q = q.children[ord(target[j]) - ord("a")]
                if p is None or q is None:
                    break
                if p.v < 0 or q.v < 0:
                    continue
                res = min(res, dfs(j + 1) + g[p.v][q.v])
            return res
        
        ans = dfs(0)
        return -1 if ans >= float('inf') else ans
