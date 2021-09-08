import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
20 1000
4
51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n, l = map(int, input().split())
k = int(input())
A = list(map(int, input().split()))

def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    start = 0
    count = 0
    for a in A:
        if a >= arg + start:
            count += 1
            start = a
            if count == k:
                if l - a >= arg:
                    return True
    pass


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ideal_len = l // (k + 1)
ans = meguru_bisect(  ideal_len + 1 , 0)
print(ans)