class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        num = Make_list(n)
        num_len = len(num)
        if num_len < k:
            return -1
        else:
            return num[k-1]
        
# 約数のリスト作成を行う関数
def Make_list(N):
    num = []
    for i in range(1,N+1):
        if N % i == 0:
            num.append(i)
    return num
