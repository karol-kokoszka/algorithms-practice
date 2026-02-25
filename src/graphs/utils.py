from collections import deque

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def equals_unordered_by_val(self, other) -> bool:
        if other is None:
            return False

        visited = {}  # self-node -> other-node

        def dfs(a, b):
            if a in visited:
                return visited[a] is b

            if a.val != b.val or len(a.neighbors) != len(b.neighbors):
                return False

            visited[a] = b

            na = sorted(a.neighbors, key=lambda x: x.val)
            nb = sorted(b.neighbors, key=lambda x: x.val)

            return all(dfs(x, y) for x, y in zip(na, nb))

        return dfs(self, other)
