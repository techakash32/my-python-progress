nums = [5, 2, 9, 1, 5, 6]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]>nums[j]:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
print(nums)