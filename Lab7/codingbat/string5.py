def count_code(str):
  a="co"
  b="e"
  count=0
  for i in range(len(str)-3):
    if str[i:i+2]==a and str[i+3]==b:
      count+=1
      
  return count