def average(nums):
    avg= [x for x in nums if x%2==0 and x%3==0]
    if len(avg)==0:
        return 0
    else:
        res = sum(avg)//len(avg)
        return res

nums=[1,3,6,10,12,15]
print(average(nums))