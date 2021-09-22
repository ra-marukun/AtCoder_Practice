import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
10 2
1 2 3 4 4 3 2 1 2 3

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from collections import defaultdict

n, k = map(int, input().split())
A = list(map(int, input().split()))

r = 0
ans = 0
unique = 0
count = defaultdict(int)

#尺取り法
for l in range(n):
    while (r < n):
        if count[A[r]] == 0: #まだA[r]が対象範囲になかった場合
            if unique == k: #k種類あったら、whileをbreak
                break
            unique += 1 # k種類以下なら、種類を増やす

        #伸びる処理(A[r]の値のカウンターを増やす)
        count[A[r]] += 1
        r += 1

    ans = max(ans, r-l)
    #縮む処理
    count[A[l]] -= 1
    if count[A[l]] == 0:
        unique -= 1
    
print(ans)