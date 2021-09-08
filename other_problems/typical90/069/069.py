import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
2021 617

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n, k = map(int, input().split())

mod = 10**9 + 7

def mod_calc(a , b):
    binb = bin(b)[2:]
    mods = [0] * len(binb)
    mods[0] = a % mod
    for i in range(1, len(mods)):
        mods[i] = (mods[i-1] % mod) ** 2
    ret = 1
    for i in range(len(mods)):
        if binb[len(binb)- i -1] == '1':
            ret = ret * mods[i] % mod
    return ret


if n == 1:
    print(k % mod)
elif n == 2:
    print( ( k % mod ) * ( ( k - 1 ) % mod ) % mod )
else:
    bin ( n - 2 )
    ans = (k%mod) * ((k-1)%mod) * mod_calc((k-2), n-2) % mod
    print(ans)

    ##以下はTLEのコード（手計算では使えるが競プロではだめ）
    # amari = (n-2) % (mod - 1)
    # ans = (k%mod) * ((k-1)%mod) * ((k-2)%mod)**(amari) % mod
    # print(ans)