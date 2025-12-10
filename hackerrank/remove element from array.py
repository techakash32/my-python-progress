nums = [0,0,1,1,1,2,2,3,3,4]
if not nums:
    print("false")
i=0
while i<len(nums)-1:
    if nums[i]==nums[i+1]:
        nums.pop(i+1)
    else:
        i+=1
print(len(nums))