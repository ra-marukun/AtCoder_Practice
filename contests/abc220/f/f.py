import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
6
1 6
1 5
1 3
1 4
1 2

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n = int(input())
m = n - 1

def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]= min(d[i][j],d[i][k]+d[k][j])
    return d



# 隣接行列の定義、初期化
# ①コスト(存在しないときはinf)
d = [[float("inf") for i in range(n)] for i in range(n)]

# ②自分自身へのコストは０
for i in range(n):
    d[i][i] = 0

# コスト入力（何もないときは１，問題によっては入力時に指定される）
cost = 1
for i in range(m):
    a,b = map(int,input().split())
    d[a-1][b-1] = cost
    d[b-1][a-1] = cost

# output
w_d = warshall_floyd(d)
print(w_d)

for i in range(n):
    print(sum(w_d[i]))
