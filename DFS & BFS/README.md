----dfs.py----

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
            
dfs algoritma di atas:
Pertama kali memeriksa apakah node saat ini tidak dikunjungi(not in visited) - jika ya, itu ditambahkan dalam set yang dikunjungi.
Kemudian untuk setiap neighbor dari node saat ini, fungsi dfs dipanggil lagi.
Kasus dasar dipanggil ketika semua node dikunjungi. Fungsi tersebut kemudian dikembalikan

----bfs.py----

import collections

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

Pertama-tama memanggil library collections

visited adalah daftar yang digunakan untuk melacak node yang dikunjungi.
queue adalah daftar yang digunakan untuk melacak node yang saat ini berada dalam antrian.
visited menambahkan root

Kemudian, sementara queue berisi elemen yang akan terus mengeluarkan node dari queue, menambahkan neighbor dari node itu ke queue 
jika neighbour tidak dikunjungi(not in visited), neighbour akan ditambahkan ke visited dan ke queue.
Ini berlanjut sampai queue kosong.

---main.py----

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

Pertama-tama memanggil class dfs dan bfs dari dfs dan bfs module

graph adalah struktur data kamus yang menggunakan adjacency list, graph telah berisi node.

visited adalah himpunan yang digunakan untuk melacak node yang dikunjungi.

Kemudian, menampilkan dfs dan bfs:

Fungsi dfs dipanggil dan melewati set visited, graph dalam bentuk data kamus, dan A, yang merupakan node awal.
Fungsi bfs dipanggil dan melewati graph dalam bentuk data kamus, dan A, yang merupakan node awal.