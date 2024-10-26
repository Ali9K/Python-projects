# FIRST STATE: define data structure
network = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Diana'],
    'Charlie': ['Alice', 'Eve'],
    'Diana': ['Bob'],
    'Eve': ['Charlie']
}
# SECONDE STATE: DFS
def DFS(network, start, visited=None):
    if visited is None:
      visited = set()
      visited.add(start)
      for following in network[start]:
            if following not in visited:
                  DFS(network, following, visited)

