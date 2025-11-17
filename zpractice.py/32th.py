nums = [10, 20, 30, 40, 50]
sum=0
average=0
for i in range(len(nums)):
    sum=sum+nums[i]
average=sum//len(nums)
print(average)