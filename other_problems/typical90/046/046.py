import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
20
238 395 46 238 264 114 354 52 324 14 472 64 307 280 209 24 165 194 179 248
270 83 377 332 173 21 362 75 66 342 229 117 124 481 48 235 376 13 420 74
175 427 76 278 486 169 311 47 348 225 41 482 355 356 263 95 170 156 340 289

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from collections import Counter

n = int(input())
A = map(int, input().split())
B = map(int, input().split())
C = map(int, input().split())

A = list(map(lambda x: x%46, A))
B = list(map(lambda x: x%46, B))
C = list(map(lambda x: x%46, C))

Acounter = Counter(A)
Bcounter = Counter(B)
Ccounter = Counter(C)

Aset = set(A)
Bset = set(B)
Cset = set(C)

ans = 0
for a in Aset:
    for b in Bset:
        for c in Cset:
            if (a + b + c)%46 == 0:
                ans += Acounter[a] * Bcounter[b] * Ccounter[c]
print(ans)