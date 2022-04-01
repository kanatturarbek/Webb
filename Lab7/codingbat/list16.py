def rotate_left3(nums):
  a=nums[0]
  nums.remove(a)
  nums.append(a)
  return nums