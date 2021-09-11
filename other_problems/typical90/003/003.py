import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
10
1 2
1 3
2 4
4 5
4 6
3 7
7 8
8 9
8 10

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import sys
from collections import deque
import numpy as np

n = int(input())

G = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)


#頂点v0から各頂点への距離を求めるbfs
def bfs(v0):
    dist = [-1]*(n+1)
    dist[0], dist[v0] = 0, 0
    d = deque()
    d.append(v0)
    while d:
        v = d.popleft()
        for i in G[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)
    return dist

nxt = np.argmax(bfs(1))
ans = np.max(bfs(nxt)) + 1
print(ans)