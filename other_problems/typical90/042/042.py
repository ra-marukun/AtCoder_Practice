import io
import sys

# ここに入力テキストを入れる
_INPUT = """\
9

"""
sys.stdin = io.StringIO(_INPUT)

# ここ以降にコーディング
k = int(input())
mod = 10**9 + 7
# dp[各桁の和] = 通り数
dp = [0] * (k + 1)
dp[0] = 1
if not k % 9 == 0:
    print(0)
else:
    for i in range(1, k + 1):
        # 9未満の場合は0なので無視して良い
        m = min(9, i)

        # Kまでのすべての値に対して、"K-1" から "K-9" までの通り数の和を求めていく
        for j in range(1, m + 1):
            dp[i] += dp[i - j]
            dp[i] %= mod

    print(dp[k])
