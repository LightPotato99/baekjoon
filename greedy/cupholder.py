n = int(input())
mystr = input()
s = mystr.count("S")
l = mystr.count("LL")
print(min(n, 1+s+l))