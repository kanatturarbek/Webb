def last2(str):
  a=str[len(str)-2:len(str)]
  count=0
  for i in range (0,len(str)-2):
    if str[i:i+2]==a:
      count+=1
  return count
