class MergingCommunities:
    _parent = []  # leads to the parent of x - eventually root = community it belongs to
    _size = []    # size[find(x)] - size of the community where x belongs to

    def __init__(self, n: int):
        for i in range(n):
            self._parent.append(i)
            self._size.append(1)

    def _find(self, x: int) -> int:
        temp = x
        while self._parent[temp] != temp:
            temp = self._parent[temp]
        return temp

    def connect(self, x: int, y: int) -> None:
        commX = self._find(x)
        commY = self._find(y)
        if commX == commY:
            return
        self._parent[x] = commY
        self._size[commY] += self._size[commX]
 
    def get_community_size(self, x: int) -> int:
        return self._size[self._find(x)]