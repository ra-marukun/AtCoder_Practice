import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
6783 125

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import math

n, l = map(int, input().split())

k = n // l

ans = 0
for i in range(k+1):
    a = n - i * l
    b = i
    c = math.factorial(a+b) // (math.factorial(a) * math.factorial(b))
    ans += c % (10**9 + 7)
print(ans%(10**9 +7))