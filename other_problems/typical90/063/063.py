import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
4 6
1 1 1 1 1 2
1 2 2 2 2 2
1 2 2 3 2 3
1 2 3 2 2 3

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from itertools import product
from collections import Counter

def calc(A: list) -> int:
    "良いグリッドを求める"

    # bitの立っている行数を求める
    colum = 0
    for i in range(len(A)):
        if A[i] == 1:
            colum += 1
     
    cnt = Counter()
    for i in range(w):
        num = [] 
        for j in range(h):
            if A[j] == 1:
                num.append(p[j][i])
        # 列に入っている数字が全て同じである時
        if len(set(num)) == 1:
            cnt[num[0]] += 1
   
    return max(cnt.values()) * colum if len(cnt) > 0 else 0

h, w = map(int,input().split())
p = [list(map(int,input().split())) for _ in range(h)]

ans = 0
for bit in product([0, 1], repeat = h):
    ans = max(ans, calc(bit))
    

print(ans)