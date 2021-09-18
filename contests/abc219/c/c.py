import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
zyxwvutsrqponmlkjihgfedcba
5
a
ab
abc
ac
b

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
X = input()
n = int(input())

S = [input() for _ in range(n)]

def function_x(St):
    ans = [0]*10
    for i,s in enumerate(St):
        val = X.index(s)+1
        ans[i] = val
    return ans

sortS =  sorted(S, key=function_x)
for i in range(n):
    print(sortS[i])
