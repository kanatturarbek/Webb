def end_other(a, b):
  if a[-len(b):].lower()==b.lower() or b[-len(a):].lower()==a.lower():
    return True
  return False