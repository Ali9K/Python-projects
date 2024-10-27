# FIRST STATE: defint data structure
network = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Diana'],
    'Charlie': ['Alice', 'Eve'],
    'Diana': ['Bob'],
    'Eve': ['Charlie']
}

def DFS(network, start, visited=None, path=None, depth= 0, depths=None):
    if visited is None:
      visited = set()
    if path is None:
         path = []
    if depths is None:
         depths = {}

    visited.add(start)
    path.append(start)
    depths[start] = depth
    print(f"{start} at depth {depth}")
    
    for following in network[start]:
        if following not in visited:
                DFS(network, following, visited, path, depth+1, depths)
    return path, depths

path, depth_info = DFS(network, 'Alice')
print("DFS Traversal Path:", path)
print("Nodes and their Depths:", depth_info)
