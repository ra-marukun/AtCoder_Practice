import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
630 940 314

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import sys
a, b, c = map(int, input().split())
for i in range(1,1001):
    num = i*c
    if a<=num<=b:
        print(num)
        sys.exit()
    if num>b:
        break
print(-1)
