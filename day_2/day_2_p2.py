
def is_safe(lis):
  isOrdered = (lis == sorted(lis) or lis == sorted(lis,reverse=True))
  
  safe = True
  for i in range(len(lis)-1):
    if abs(lis[i]-lis[i+1]) <=3 and lis[i] != lis[i+1]:
      continue
    else:
      safe = False
  
  return isOrdered and safe
    

if __name__ == "__main__":

  grid = []
  for line in open("input.txt",'r').readlines():
    # print(line.split())
    grid.append(list(map(int,line.split())))

  # print(grid)
  
  res = 0
  
  for row in grid:
    
    if is_safe(row):
      res += 1
      continue
    
    safe = False
    for i in range(len(row)):
      if is_safe(row[:i] + row[i+1:]): 
        safe = True
    
    if safe == True:
      res += 1
  print(res)
      
  