if __name__ == "__main__":

  grid = []
  for line in open("input.txt",'r').readlines():
    # print(line.split())
    grid.append(list(map(int,line.split())))

  # print(grid)
  
  res = 0
  for row in grid:
    safe = 1
    for i in range(len(row)-1):
      if abs(row[i]-row[i+1]) <=3 and row[i] != row[i+1]:
        continue
      else:
        safe = 0
      
    asc = 1 if row[i] < row[i+1] else 0
    
    if asc == 1:
      for i in range(len(row)-1):
        if row[i] > row[i+1]:
          safe = 0
    else:
      for i in range(len(row)-1):
        if row[i] < row[i+1]:
          safe = 0
    
    if safe == 1:
      res+=1
      
  print(res)
      
  