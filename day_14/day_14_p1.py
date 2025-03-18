from collections import defaultdict , deque

def getProdFromQuadrants(robots, width, height):
  # Create a 2D grid to represent the quadrants
  grid = [[0 for i in range(width)] for j in range(height)]
  for rt in robots:
    grid[rt[0][1]][rt[0][0]] += 1
    # Define the four quadrants
  # print(grid)
  q1 = []
  q2 = []
  q3 = []
  q4 = []
  for i in range(height):
    for j in range(width):
      if i < height // 2 and j < width // 2:
        q1.append(grid[i][j])
      elif i < height // 2 and j > width // 2 :
        q2.append(grid[i][j])
      elif i > height // 2 and j < width // 2:
        q3.append(grid[i][j])
      elif i > height // 2  and j > width // 2 :
        q4.append(grid[i][j])
  # print(q1)
  # print(q2)
  # print(q3)
  # print(q4)
  
  return [sum(q1),sum(q2),sum(q3),sum(q4)]
      

if __name__ == "__main__":

  grid = []
  for line in open("input.txt",'r').readlines():
    # print(line.split())
    grid.append(line.split())
  
  # print(grid)
  
  robots = []
  
  for rob in grid:
    pos = list(map(int,(rob[0].split('=')[1].split(','))))
    vel = list(map(int,(rob[1].split('=')[1].split(','))))
    robots.append([pos,vel])

  time = 100
  w=101
  h=103
  for rt in robots:
    xvel = rt[1][0]
    yvel = rt[1][1]
    rt[0][0] += xvel*time
    rt[0][1] += yvel*time
    rt[0][0] = rt[0][0]%w
    rt[0][1] = rt[0][1]%h
  
  res = getProdFromQuadrants(robots,w,h)
  # print(res)
  ans = 1
  for i in res:
    ans *= i
  print(ans)