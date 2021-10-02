import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
998244353

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n = int(input())

keta = len(str(n))

def change_big(l):
    num = []
    str_n = str(n)
    for i in l:
        num.append(str_n[i])
    num = sorted(num,reverse = True)
    num = int(''.join(map(str, num)))
    return num

ans = 0
for i in range(1,2**keta-1):
    s = format(i,'0{}b'.format(keta))
    list_1 = [j for j, x in enumerate(s) if x == '1']
    list_2 = [j for j, x in enumerate(s) if x == '0']
    num1 = change_big(list_1)
    num2 = change_big(list_2)
    ans = max(num1*num2,ans)
print(ans)