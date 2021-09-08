import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
8
1 4
1 3
1 2
1 1
3
2
1 0
2

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from sys import stdin
from collections import deque

q = int(input())
J = [list(map(int, stdin.readline().split())) for _ in range(q)]

d = deque()

for j in J:
    if j[0]==1:
        d.append(j[1])
    elif j[0] == 2:
        print(d.popleft())
    else:
        l = list(d)
        l = sorted(l)
        d = deque(l)