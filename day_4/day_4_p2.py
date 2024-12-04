

if __name__ == "__main__":

  grid = []
  for line in open("input.txt",'r').readlines():
    # print(line.split())
    grid.append(line.split()[0])
    
  # print(grid)
  n = len(grid)
  m = len(grid[0])
  
  res = 0

  for r in range(n):
    for c in range(m):

        if r+2<n and c+2<m and grid[r][c]=='M' and grid[r+1][c+1]=='A' and grid[r+2][c+2]=='S' and grid[r+2][c]=='M' and grid[r][c+2]=='S':
            res += 1
        if r+2<n and c+2<m and grid[r][c]=='M' and grid[r+1][c+1]=='A' and grid[r+2][c+2]=='S' and grid[r+2][c]=='S' and grid[r][c+2]=='M':
            res += 1
        if r+2<n and c+2<m and grid[r][c]=='S' and grid[r+1][c+1]=='A' and grid[r+2][c+2]=='M' and grid[r+2][c]=='M' and grid[r][c+2]=='S':
            res += 1
        if r+2<n and c+2<m and grid[r][c]=='S' and grid[r+1][c+1]=='A' and grid[r+2][c+2]=='M' and grid[r+2][c]=='S' and grid[r][c+2]=='M':
            res += 1
  
  print(res)
  
