import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
100000000
10001 10002 10003

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング

n = int(input())
l = list(map(int, input().split()))

l.sort()
a, b, c = l[2], l[1], l[0]


ans = 10000
for i in range(10000):
    for j in range(10000-i):
        if (n - a * i - b * j) < 0:
            break
        if (n - a * i - b * j) % c == 0:
            k = (n - a * i - b * j) // c
            if i + j + k < ans:
                ans = i + j + k
print(ans)