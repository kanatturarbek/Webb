def count_hi(str):
  a="hi"
  count=0
  for i in range(len(str)):
    if str[i:i+2]==a:
      count+=1
  return count
