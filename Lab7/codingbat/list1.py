def count_evens(nums):
  count=0
  for i in nums:
    if i%2==0 or i==0:
      count+=1
  return count