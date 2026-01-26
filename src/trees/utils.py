from __future__ import annotations

from typing import Optional, Sequence


class TreeNode:
    def __init__(self, val: Optional[int] = None, *, slice: Optional[Sequence[Optional[int]]] = None):
        self.val: Optional[int] = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

        if slice is None:
            if val is None:
                raise TypeError("TreeNode() requires either 'val' or 'slice'.")
            return

        if len(slice) == 0:
            raise ValueError("'slice' must contain at least one element.")

        if slice[0] is None:
            raise ValueError("Root value cannot be None; use root=None to represent an empty tree.")

        # Build using array-indexed representation (heap-style):
        # children of index i are (2*i+1) and (2*i+2).
        self.val = slice[0]
        nodes: list[Optional[TreeNode]] = [None] * len(slice)
        nodes[0] = self

        for i in range(1, len(slice)):
            v = slice[i]
            nodes[i] = TreeNode(v) if v is not None else None

        for i, node in enumerate(nodes):
            if node is None:
                continue
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < len(nodes):
                node.left = nodes[li]
            if ri < len(nodes):
                node.right = nodes[ri]

    def __eq__(self, other):
        if other is None:
            return False

        if not isinstance(other, TreeNode):
            return False

        return (
            self.val == other.val and
            self.left == other.left and
            self.right == other.right
        )
    
    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    def __ne__(self, other):
        return not self.__eq__(other)