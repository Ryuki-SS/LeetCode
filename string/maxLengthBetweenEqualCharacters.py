class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dict = {}
        res = -1
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = [i, i]
            else:
                dict[s[i]][1] = i
        for value in dict.values():
            length = value[1] - value[0] - 1
            if length > res:
                res = length
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.maxLengthBetweenEqualCharacters('asdgqa'))
