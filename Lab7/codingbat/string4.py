def cat_dog(str):
  count1=0
  count2=0
  a="cat"
  b="dog"
  for i in range(len(str)):
    if str[i:i+3]==a:
      count1+=1
    if str[i:i+3]==b:
      count2+=1
  if count1==count2:
    return True
  else:
    return False