import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
4 5 0
2 3 2 1 4
1 2
2 3
3 4

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from collections import deque

n, m ,k = map(int, input().split())
A = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(n-1)]

vec = [0] * (n)

Node = [[] for i in range(n+1)]
for i in range(1, n):
    a,b = edges[i-1][0],edges[i-1][1]
    Node[a].append(b)
    Node[b].append(a)

for i in range(m-1):
    cur = A[i]
    nxt = A[i+1]

    