import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
3 3
10
1 2 2
1 1 1
2 1 1 2 2
1 3 2
2 1 1 2 2
2 2 2 3 2
1 2 3
1 2 1
2 1 1 2 2
2 1 1 3 3

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from collections import defaultdict

class UnionFind():
    
    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        """
        ノードxの根を見つける

        Parameters
        ---------------------
        x : int
            見つけるノード

        Returns
        ---------------------
        root : int
            根のノード
        """
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合

        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        """
        同じグループに属するか判定

        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード

        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        木のサイズを計算

        Parameters
        ---------------------
        x : int
            計算したい木のノード

        Returns
        ---------------------
        size : int
            木のサイズ
        """
        return -self.root[self.find(x)]

    def roots(self):
        """
        根のノードを取得

        Returns
        ---------------------
        roots : list
            根のノード
        """
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        """
        グループ数を取得

        Returns
        ---------------------
        size : int
            グループ数
        """
        return len(self.roots())

    def group_members(self):
        """
        全てのグループごとのノードを取得

        Returns
        ---------------------
        group_members : defaultdict
            根をキーとしたノードのリスト
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


h, w = map(int, input().split())
Q = int(input())

cnt = 0
dic= {}
for i in range(h):
    for j in range(w):
        dic[cnt] = 0
        cnt += 1

uf = UnionFind(h*w+1)
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:#クエリ1 点の追加
        idx = ( q[1] -1 ) * w + q[2] - 1
        dic[idx] = 1
        if q[1]  >= 2:
            if dic[idx-w]==1:
                uf.unite(idx-w+1,idx+1)
        if q[2]  >= 2:
            if dic[idx-1]==1:
                uf.unite(idx,idx+1)
        if q[2] <= w-1:
            if dic[idx+1]==1:
                uf.unite(idx+2,idx+1)
        if q[1] <= h-1:
            if dic[idx+w]==1:
                uf.unite(idx+w+1,idx+1)

    else:
        idx1 = ( q[1] -1 ) * w + q[2] - 1
        idx2 = ( q[3] -1 ) * w + q[4] - 1
        if (dic[idx1]==0)|(dic[idx2]==0):
            print('No')
        else:
            if uf.same(idx1+1,idx2+1):
                print('Yes')
            else:
                print('No')

