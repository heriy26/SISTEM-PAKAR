from Test.dfs import dfs
from Test.bfs import bfs

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []}
visited = set()

print("Hasil Depth First Search:")
dfs(visited, graph, 'A')

print("Hasil Breadth First Search:")
bfs(graph, 'A')
