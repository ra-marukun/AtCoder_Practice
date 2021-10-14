import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
2 2
GC
PG
CG
PP

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n , m = map(int,input().split())
A = [list(input()) for _ in range(2*n)]

wins = [0] * (2*n)
junni = [0] * (2*n)

for i in range(2*n):
    wins[i] = (2*n - i - 1) / (2*n)
    junni[i] = i+1

def one_round(round):
    for i in range(n):
        one_idx = junni[2 * i] - 1
        two_idx = junni[2 * i + 1] - 1

        one = A[one_idx][round]
        two = A[two_idx][round]
        if one == two:
            continue
        else:
            if (one == 'G') & (two == 'C'):
                wins[one_idx] += 1
            elif (one == 'C') & (two == 'P'):
                wins[one_idx] += 1
            elif (one == 'P') & (two == 'G'):
                wins[one_idx] += 1
            else:
                wins[two_idx] += 1

def judge(i):
    return wins[i-1]

for i in range(m):
    one_round(i)
    junni = sorted(junni,key = judge,reverse = True)

for i in range(2*n):
    print(junni[i])