from src.graphs.utils import GraphNode

def graph_deep_copy(node: GraphNode) -> GraphNode:
    if not node:
        return None
    return dfs_copy(node)

def dfs_copy(node: GraphNode, cloned_map = {}) -> GraphNode:
    if id(node) in cloned_map:
        return cloned_map[id(node)]
    
    cloned_node = GraphNode(node.val)
    cloned_map[id(node)] = cloned_node
    
    for n in node.neighbors:
        cloned_node.neighbors.append(dfs_copy(n, cloned_map))
    
    return cloned_node