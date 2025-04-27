comp = 0
start = 1
end = 5
while start <= end:
    mid = start +(end - start)//2
    if (mid * (mid + 1)) // 2 <= 5:
        comp = mid
        start = mid + 1
    else:
        end = mid - 1
print(comp)