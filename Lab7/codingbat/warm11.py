def front_back(str):
  if len(str)<=1:
    return str
  a=str[0]
  b=str[len(str)-1]
  c=str[1:len(str)-1]
  
  return b+c+a