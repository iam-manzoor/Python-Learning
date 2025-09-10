# Sum of n natural numbers using recursive function

def cal_sum(n):
  if n == 0:
    return
  return cal_sum(n-1) + n

print(cal_sum(5))
    
