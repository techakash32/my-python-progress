nums=[0,0,1,1,1,2,2,3,3,4]
if not nums:
    print("0")
i=0
for j in range(1,len(nums)):
    if nums[j]!=nums[i]:
        i+=1
        nums[i]=nums[j]
print(i+1)
        