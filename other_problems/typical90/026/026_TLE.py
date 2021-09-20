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
import sys
sys.setrecursionlimit(10**5)
from collections import deque

n = int(input())
dict = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    dict[a].append(b)
    dict[b].append(a)

def dfs(v,c):
    if(len(color1)>=n//2):
        for _ in range(n//2):
            print('{} '.format(color1.popleft()),end='')
        sys.exit()
    elif(len(color2)>=n//2):
        for _ in range(n//2):
            print('{} '.format(color2.popleft()),end='')
        sys.exit()
    else:
        queue[v] = 1
        for i in dict[v]:#vの隣接点に関して
            if queue[i] == 0:
                if c==1:
                    color2.append(i)
                else:
                    color1.append(i)
                dfs(i,1 - c)

  
color1 = deque()
color2 = deque()
queue = [0 for _ in range(n+1)]
color1.append(1)
(dfs(1,1))
