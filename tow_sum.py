


def twoSum_bruteforce(nums,target):
    for x in range(len(nums)):
        for y in range(x+1,len(nums)):
            if nums[x]+nums[y]==target:
                return[x,y]


def twoSum(nums,target):
    seen={}
    for x in range(len(nums)):
        y = target - nums[x]
        if y not in seen:
            seen[nums[x]]= x
        else :
            return(x,seen[y])
        
print(twoSum(nums = [2,6,7,11,15], target = 9))