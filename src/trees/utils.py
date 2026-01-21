class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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