import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
3
1 18 1

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import numpy as np

n= int(input())
A = list(map(int, input().split()))

A = np.array(A)
ruiseki = [0] * (2*n + 1)
ruiseki = np.array(ruiseki)
ruiseki[1:n+1] = np.cumsum(A)
size = ruiseki[n]
ruiseki[n+1:2*n+1] = ruiseki[1:n+1] + size

target = size / 10

def isOK(index, key):
    if ruiseki[index] >= key:
        return True
    else:
        return False


def binary_search(key, i):
    ng = i -1
    ok = i + n +1

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        
        if isOK(mid, key):
            ok = mid
        else:
            ng = mid

    return ok


def judge(i):
    point = binary_search(ruiseki[i] + target, i)
    if (ruiseki[point]-ruiseki[i]) == target:
        return True
    else:
        return False

if not(size % 10 == 0):
    print('No')
else:
    for i in range(1,n + 1):
        if ruiseki[i+1] - ruiseki[i] > target:
            if i == n:
                print('No')
            continue
        elif judge(i):
            print('Yes')
            break
        elif i == n:
            print('No')