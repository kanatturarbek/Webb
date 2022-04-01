def caught_speeding(speed, is_birthday):
  if (is_birthday==True and speed >85) or (is_birthday==False and speed >80) :
    return 2
  elif (is_birthday==True and speed>=66 and speed<=85) or (is_birthday==False and speed >=61 and speed<=80) :
    return 1    
  if (is_birthday==True and speed <=65) or (is_birthday==False and speed <=60) :
    return 0