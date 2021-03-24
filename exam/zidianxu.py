str = input()
for i in range(len(str)):
    if str[i] > str[i - 1]:
        m = str[i]
        index = i
        for j in range(i + 1, len(str)):
            if str[j] < m:
                m = str[j]
                index = j
        if m < str[i]:
            s = str[:i] + str[index] + str[i + 1 : index] + str[i] + str[index + 1 :]
            print(s)
            exit()


# aaazbcdeadcd
# 样例输出
# aaaabcdezdcd

"""
题目描述：
给一个字符串s，你可以至多选择两个不同位置的字符进行交换（可以选择不交换，保留原串），问所有可能中字典序最小的串。

有关字典序：对于长度相同的串a和串b，串a的字典序小于串b当且仅当存在一个位置i使得串a和串b的前i-1个字符完全相同且串a的第i个字符小于串b的第i个字符。即a1=b1,a2=b2,...ai-1=bi-1且ai<bi。



输入描述
一行一个字符串s，保证串中都为小写字母('a'~'z')。字符串长度<=200000

输出描述
输出一个串t，表示所有可能中字典序最小的串。


样例输入
aaazbcdeadcd
样例输出
aaaabcdezdcd

"""
