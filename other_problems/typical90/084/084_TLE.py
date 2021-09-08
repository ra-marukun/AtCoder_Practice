import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
7
xxoooxx

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from collections import deque
import numpy as np
n = int(input())
s = input()
 
s_start = s[0]
if s_start == 'x':
    s_else = 'o'
else:
    s_else = 'x'
 
s_0 = list(map(len, s.split(s_else)))
s_1 = list(map(len, s.split(s_start)))
s_0 = deque(s_0)
s_1 = deque(s_1)

while 0 in s_0:
    s_0.remove(0)
while 0 in s_1:
    s_1.remove(0)

d = deque()
while (len(s_0)!=0):
    d.append(s_0.popleft())
    if (len(s_1)!=0):
        d.append(s_1.popleft())
l = np.array(d)
csum = np.cumsum(l)
csum_end = csum[-1]
 
ans = 0
for i in range(len(l)):
    ans += l[i] * (csum_end - csum[i])
print(ans)