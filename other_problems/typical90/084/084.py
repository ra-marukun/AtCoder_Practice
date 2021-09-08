import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
7
xxoooxx

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from itertools import groupby
import numpy as np
n = int(input())
s = input()
 

def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append(int(len(list(v))))
        # res.append((k, int(len(list(v)))))
    return res

d = runLengthEncode(s)
l = np.array(d)
csum = np.cumsum(l)
csum_end = csum[-1]
 
ans = 0
for i in range(len(l)):
    ans += l[i] * (csum_end - csum[i])
print(ans)