def alarm_clock(day, vacation):
  if (day==6 or day==0) and vacation==True:
    return 'off'
  elif ((day==6 or day==0) and vacation==False )or (day>0 and day<6 and vacation==True):
    return '10:00'
  else:
    return '7:00'