import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
5
1000000000 1000000000
1000000000 1000000000
100 1
100 10
105 120

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n = int(input())

xy = [map(int, input().split()) for _ in range(n)]
A, B = [list(i) for i in zip(*xy)]
C = [0]*(2*n)
F = [0]*n
for i in range(n):
    C[2*i] = A[i]
    C[2*i+1] = A[i] + B[i] 
    F[i] = A[i] + B[i] 

E = sorted(set(C))

# B の各要素が何番目の要素なのかを辞書型で管理する
D = { v: i for i, v in enumerate(E) }

zipA = [0]*n
zipC = [0]*n

for i in range(n):
    zipA[i] = D[A[i]]
    zipC[i] = D[F[i]]


day_max = max(zipC)

temp = [0]*(day_max+1)

for i in range(n):
    minday = zipA[i]
    maxday = zipC[i]
    temp[minday] += 1
    if maxday<=day_max:
        temp[maxday] -= 1

def np_x_zeta(x, initial=None):
    if isinstance(x[0], list):
        for i in range(len(x)):
            np_x_zeta(x[i], initial=initial)
        if initial is not None:
            x.insert(0, [initial] * len(x[0]))
        for j in range(len(x[0])):
            for i in range(1, len(x)):
                x[i][j] += x[i - 1][j]
    else:
        if initial is not None:
            x.insert(0, initial)
        for i in range(1, len(x)):
            x[i] += x[i - 1]

np_x_zeta(temp)

cnt = [0]*(n+1)


day_list = list(D.keys())
for i in range(day_max):
    cnt[temp[i]] += day_list[i+1] - day_list[i]

print(*cnt[1:])
