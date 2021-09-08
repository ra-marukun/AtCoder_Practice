import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
48

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr



lists = factorization(n)
print(lists)
beki = -1
for l in lists:
    beki += l[1]

s = bin(beki)[2:]
if beki == 0:
    print(0)
else:
    print(len(s))