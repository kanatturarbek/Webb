def max_end3(nums):
  l=list()
  if nums[0]>nums[len(nums)-1]:
    l.append(nums[0])
    l.append(nums[0])  
    l.append(nums[0])
  else:
    l.append(nums[len(nums)-1])
    l.append(nums[len(nums)-1])  
    l.append(nums[len(nums)-1])
    
  return l