# 杨辉三角
# class Solution:
#     def generate(self, numRows: int) -> list[list[int]]:
#         res = [[] for _ in range(numRows)]
#         res[0].append(1)
#         for i in range(1, numRows):
#             res[i].append(1)
#             for j in range(1, i):
#                 res[i].append(res[i - 1][j - 1] + res[i - 1][j])
#             res[i].append(1)
#         return res


# class Solution:
#     def generate(self, numRows: int) -> list[list[int]]:
#         res = list()
#         for i in range(0, numRows):
#             tem = list()
#             for j in range(0, i + 1):
#                 if j == 0 or j == i:
#                     tem.append(1)
#                 else:
#                     tem.append(res[i - 1][j - 1] + res[i - 1][j])
#             res.append(tem)
#         return res


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1] * (i + 1) for i in range(numRows)]
        if numRows < 3:
            return res
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.generate(5))
