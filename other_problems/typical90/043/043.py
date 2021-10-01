import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
4 6
2 1
1 5
...#..
.#.##.
.#....
...##.

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from collections import deque

h,w = map(int, input().split())
rs,cs = map(int, input().split())
rt,ct = map(int, input().split())

A = []
A.append(['#']*(w+2) )
A.extend([ ['#']+list(input())+['#'] for _ in range(h) ]) 
A.append(['#']*(w+2))

INF = 10**18
dist = [[[INF] * 4 for _ in range (w+2)] for _ in range(h+2)]
for i in range(4):
    dist[rs][cs][i] = 0

q = deque()
for i in range(4):
    q.append([rs,cs,i])

d = [[0,1],[1,0],[0,-1],[-1,0]]

while q:
    vy,vx,muki = q.popleft()

    for i, (dy,dx) in enumerate(d):
        if A[vy+dy][vx+dx] == '#':
            continue
        if i == muki:
            if dist[vy+dy][vx+dx][i] > dist[vy][vx][muki]:
                dist[vy+dy][vx+dx][i] = dist[vy][vx][muki]
                q.appendleft([vy+dy,vx+dx,i])
        else:
            if dist[vy+dy][vx+dx][i] > dist[vy][vx][muki]+1:
                dist[vy+dy][vx+dx][i] = dist[vy][vx][muki]+1
                q.append([vy+dy,vx+dx,i])

ans = INF
for i in range(4):
    ans = min(dist[rt][ct][i],ans)
print(ans)