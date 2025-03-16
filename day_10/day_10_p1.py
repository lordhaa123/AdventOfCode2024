from collections import defaultdict

if __name__ == "__main__":

  grid = []
  for line in open("input.txt",'r').readlines():
    # print(line.split())
    grid.append(line.split()[0])
  
  # print(grid)
  
  temp = []
  for i in grid:
    temp.append(list(map(int,list(i))))
  grid = temp
  # print(grid)

  start = []

  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 0:
        start.append((i,j))
  
  n = len(grid)
  m = len(grid[0])
  res = []
  # print(start)
  for (i,j) in start:
    vis = set()
    temp = [0]
    def dfs(i,j,curr ,temp):
      vis.add((i,j))
      if(grid[i][j] == 9):
        temp[0] += 1
        # print(i,j)
        return
      try:
        if((i+1,j) not in vis and i+1<n and grid[i+1][j] == curr+1):
          dfs(i+1,j,curr+1,temp)
      except Exception as e:
        print(i,j , "error for i+1" , e)
      try:
        if((i-1,j) not in vis and i-1>=0 and grid[i-1][j] == curr+1):
          dfs(i-1,j,curr+1,temp)
      except:
        print(i,j , "error for i-1")
      try:
        if((i,j+1) not in vis and j+1<m and grid[i][j+1] == curr+1):
          dfs(i,j+1,curr+1,temp)
      except:
        print(i,j , "error for j+1")
      try:
        if((i,j-1) not in vis and j-1>=0 and grid[i][j-1] == curr+1):
          dfs(i,j-1,curr+1,temp)
      except:
        print(i,j , "error for j-1")
    dfs(i,j,0,temp)
    res.append(temp)
  
  ans = 0
  for i in res:
    ans += i[0]
  print(ans)