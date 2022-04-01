def sum2(nums):
  end=2
  sum=0
  if len(nums)<2:
    end=len(nums)
  for i in range(end):
    sum+=nums[i]
  return sum
