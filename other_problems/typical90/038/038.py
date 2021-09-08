import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
1000000000000000000 91245533366

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import math

a, b = map(int, input().split())
g = math.gcd(a,b)
ans = a // g * b

if ans > 10**18:
    print('Large')
else:
    print(ans)