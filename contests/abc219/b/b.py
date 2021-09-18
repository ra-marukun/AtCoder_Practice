import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
a
b
c
1

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
s1 = input()
s2 = input()
s3 = input()
T = input()

ans = ''
for t in T:
    t = int(t)
    if t == 1:
        ans += s1
    elif t == 2:
        ans += s2
    else:
        ans += s3

print(ans)