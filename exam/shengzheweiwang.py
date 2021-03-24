import sys


def maxchar(n, s):
    dict = {}
    for c in s:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    m = 0
    for v in dict.values():
        if v > m:
            m = v
    l = len(s)
    oth = l - m
    for i in range(n):
        if m < l and oth > 0:
            m += 1
            oth -= 1
        else:
            m -= 1
            oth += 1
    return m


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    s3 = sys.stdin.readline().strip()
    xiaoming = maxchar(n, s1)
    xiaowang = maxchar(n, s2)
    xiaoli = maxchar(n, s3)
    if xiaoming == xiaowang or xiaoming == xiaoli or xiaowang == xiaoli:
        print("draw")
    elif xiaoming > xiaowang and xiaoming > xiaoli:
        print("xiaoming")
    elif xiaowang > xiaoming and xiaowang > xiaoli:
        print("xiaowang")
    else:
        print("xiaoli")
