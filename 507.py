n = 28
ls = []
for i in range(1,n):
    if n % i == 0:
        ls.append(i)
print(sum(ls) == n)
print(ls)
