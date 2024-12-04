

if __name__ == "__main__":

  grid = []
  for line in open("input.txt",'r').readlines():
    # print(line.split())
    grid.append(line.split()[0])
    
  # print(grid)
  n = len(grid)
  m = len(grid[0])
  def countForXmax(x,y):
    count = 0
    temp = ''

    for i in range(4):
      if y+i < m:
        temp += grid[x][y+i]
    if temp == 'XMAS':
      count+=1
      
    temp = ''
    for i in range(4):
      if y-i >= 0:
        temp += grid[x][y-i]
    if temp == 'XMAS':
      count+=1
    
    temp = ''
    for i in range(4):
      if x+i < n:
        temp += grid[x+i][y]
    if temp == 'XMAS':
      count += 1
    
    temp = ''
    for i in range(4):
      if x-i >= 0:
        temp += grid[x-i][y]
    if temp == 'XMAS':
      count += 1
       
    temp = ''
    for i in range(4):
      if x+i < n and y+i < m:
        temp += grid[x+i][y+i]
    if temp == 'XMAS':
      count += 1

    temp = ''
    for i in range(4):
      if x-i >= 0 and y-i >= 0:
        temp += grid[x-i][y-i]
        
    if temp == 'XMAS':
      count += 1
    
    temp = ''
    for i in range(4):
      if x-i >= 0 and y+i < m:
        temp += grid[x-i][y+i]
        
    if temp == 'XMAS':
      count += 1
    
    temp = ''
    for i in range(4):
      if x+i < n and y-i >= 0:
        temp += grid[x+i][y-i]
    if temp == 'XMAS':
      count += 1
    
    return count
    
  res = 0
  for i in range(n):
    # print(grid[i])
    for j in range(m):
      if grid[i][j] == 'X':
        res += countForXmax(i,j)
  
  print(res)
  
