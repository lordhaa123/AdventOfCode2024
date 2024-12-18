from collections import defaultdict

if __name__ == "__main__":

  grid = []
  for line in open("input.txt",'r').readlines():
    # print(line.split())
    grid.append(line.split()[0])
  
  mp = defaultdict(list)
  
  n = len(grid)
  m = len(grid[0])
  for r in range(n):
    for c in range(m):
      if grid[r][c] != '.':
        mp[grid[r][c]].append((r,c))
  
  antiNodes = set()
  # print(mp)
  for r in range(n):
    for c in range(m):
      for k,lis in mp.items():
        for x1,y1 in lis:
          for x2,y2 in lis:
            if (x1,y1) != (x2,y2):
              d1 = abs(r-x1) + abs(c-y1)
              d2 = abs(r-x2) + abs(c-y2)
              
              dx1 = r-x1
              dx2 = r-x2
              dy1 = c-y1
              dy2 = c-y2
              
              if (dx1*dy2 == dx2*dy1):
                antiNodes.add((r,c))
  
  # print(antiNodes)
  print(len(antiNodes))
        