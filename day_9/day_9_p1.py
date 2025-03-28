from collections import defaultdict, deque

if __name__ == "__main__":

  grid = open("input.txt",'r').read().strip()
  
  # print(grid)

  if(len(grid)%2 == 0):
    grid = grid[:-1]

  # print(grid)

  fin = []
  space = []
  val = []
  id = 0
  pos = 0

  for i,ch in enumerate(grid):
      if(i%2 == 0):
        for j in range(int(ch)):
          fin.append(id)
          val.append((pos,id))
          pos += 1
        id += 1
      else:
        space.append((pos,int(ch)))
        for i in range(int(ch)):
          fin.append(None)
          pos+=1

  # print(fin)
  for pos,id in reversed(val):
    for space_i,(spacePos,spaceSz) in enumerate(space):
      if(spacePos<pos) and spaceSz > 0:
        fin[pos] = None
        fin[spacePos] = id
        space[space_i] = (spacePos+1 , spaceSz-1)
        break



  # print(fin)
  # print(val)
  # print(space)

  ans = 0
  for i , ch in enumerate(fin):
    if ch != None:
      ans += i*ch

  print(ans)
