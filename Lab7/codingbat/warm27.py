def array_front9(nums):
  booll=False
  end=4
  if len(nums)<4:
    end=len(nums)
  for i in range(end):
    if nums[i]==9:
      booll=True
  return booll    
  