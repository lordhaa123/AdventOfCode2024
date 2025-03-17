from collections import defaultdict , deque

if __name__ == "__main__":

  grid = []
  for line in open("input.txt",'r').readlines():
    # print(line.split())
    grid.append(line.split()[0])
  
  # print(grid)
  
  p = 0
  DIRS = [(-1,0),(0,1),(1,0),(0,-1)] 
  G = grid
  R = len(G)
  C = len(G[0])

  SEEN = set()
  for r in range(R):
      for c in range(C):
          if (r,c) in SEEN:
              continue
          Q = deque([(r,c)])
          area = 0
          perim = 0
          while Q:
              r2,c2 = Q.popleft()
              if (r2,c2) in SEEN:
                  continue
              SEEN.add((r2,c2))
              area += 1
              for dr,dc in DIRS:
                  rr = r2+dr
                  cc = c2+dc
                  if 0<=rr<R and 0<=cc<C and G[rr][cc]==G[r2][c2]:
                      Q.append((rr,cc))
                  else:
                      perim += 1
          p += area*perim


  print(p)
