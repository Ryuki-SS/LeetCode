class Solution:
    def findMaxButtons(self, buttons):
        res = 0
        for i in range(len(buttons)):
            for j in range(buttons[i]):
                if j == 0:
                    res += 1
                else:
                    res += i + 1
        return res


if __name__ == "__main__":
    l = [2, 2, 2]
    a = Solution()
    print(a.findMaxButtons(l))
