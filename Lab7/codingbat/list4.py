def sum13(nums):
   nums += [0]
   return sum(n for i, n in enumerate(nums) if n != 13 and nums[i-1] != 13)