import re

if __name__ == "__main__":
  grid = []
  for line in open("input.txt",'r').readlines():
    # print(line)
    grid.append(line)
    
  # print(grid)
  
  pattern = "mul\(\d\d?\d?,\d\d?\d?\)"
  res = 0
  for row in grid:
    x = re.findall(pattern , row)
    temp = 0
    for i in x:
      s = i[4:-1]
      s = s.split(',')
      # print(s)
      temp = temp + int(s[0]) * int(s[1])
    res += temp
  
  print(res)
    
 