import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
99999 1000000000000000000

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n, k = map(int, input().split())

amari = [0] * (10**5+1)
amari[0] = n
a, b, c, d, e = map(int, list('{0:05d}'.format(n)))

for i in range(1,10**5+1):
    z = amari[i-1]
    a, b, c, d, e = map(int, list('{0:05d}'.format(z)))
    amari[i] = (z + a + b + c + d + e) % 100000


if k <= 10**5+1:
    print(amari[k])
else:
    first = amari[0:10**5-1].index(amari[10**5])
    loop = 10**5 - first
    k -= first
    k %= loop
    k += first
    print(amari[k])