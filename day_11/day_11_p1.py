from collections import defaultdict

if __name__ == "__main__":

  
  grid = open("input.txt",'r').read().split()
  
  grid = list(map(int, grid))
  # print(grid)

  def blink(x,new_grid):
    if x == 0:
      new_grid.append(1)
      return
    if len(str(x))%2 == 0:
      new_grid.append(int(str(x)[:len(str(x))//2]))
      new_grid.append(int(str(x)[len(str(x))//2:]))
      # print(x, temp)
      return
    
    new_grid.append(int(x*2024))

  for _ in range(25):
    new_grid = []
    for i in grid:
      blink(i,new_grid)
    grid = new_grid
    # print(grid)
  print(len(grid))
  
