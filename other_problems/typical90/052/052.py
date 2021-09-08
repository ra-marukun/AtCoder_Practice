import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
7
19 23 51 59 91 99
15 45 56 65 69 94
7 11 16 34 59 95
27 30 40 43 83 85
19 23 25 27 45 99
27 48 52 53 60 81
21 36 49 72 82 84

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n = int(input())
A = [list(map(int, input().split())) for l in range(n)]

ans = 1
for i in range(n):
    k = A[i][0] + A[i][1] + A[i][2] + A[i][3] + A[i][4] + A[i][5]
    ans = ans * k % (10**9 + 7)
print(ans)