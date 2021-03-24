a, b, s = map(int, input().split())
a, b = abs(a), abs(b)
if (a + b) <= s and ((a + b) - s) % 2 == 0:
    print("Yes")
else:
    print("No")

"""
a,b,s = map(int, input().split())
if (a,b)==(0,0): print("Yes")
elif abs(a)+abs(b)<=s and (s-a-b)%2==0: print("Yes")
else: print("No")
"""
