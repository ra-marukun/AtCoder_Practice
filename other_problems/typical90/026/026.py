import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
4
1 2
2 3
2 4

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from collections import deque

n = int(input())
dict = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    dict[a].append(b)
    dict[b].append(a)

def dfs(s):
    if visited[s]:
        return
    visited[s] = 1
    c = color[s]
    if c==1:
        c = 0
    else:
        c = 1

    for i in dict[s]:
        if visited[i] == 0:
            stack.append(i)
            color[i] = c
            if c == 1:
                color1.append(i)
            else:
                color2.append(i)


  
color1 = deque()
color2 = deque()
stack = deque([1])
color1.append(1)
color = [0 for _ in range(n+1)]
color[1] = 1
visited = [0 for _ in range(n+1)]

while stack:
    s = stack.pop()
    dfs(s)

if(len(color1)>=n//2):
        for _ in range(n//2):
            print('{} '.format(color1.popleft()),end='')
elif(len(color2)>=n//2):
        for _ in range(n//2):
            print('{} '.format(color2.popleft()),end='')

