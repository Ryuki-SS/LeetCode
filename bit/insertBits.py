class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        for t in range(i, j+1):
            N &= ~(1 << t)
        return N | (M << i)


if __name__ == '__main__':
    a = Solution()
    print(a.insertBits(1024, 19, 2, 6))
