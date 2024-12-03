import re

if __name__ == "__main__":
  
  grid = open("input.txt",'r').read().strip()
      
  pattern = r'mul\(\d{1,3},\d{1,3}\)'
  
  res = 0
  enabled = True
  for i in range(len(grid)):
      if grid[i:].startswith('do()'):
          enabled = True
      if grid[i:].startswith("don't()"):
          enabled = False
      instr = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', grid[i:])
      if instr is not None:
          x,y = int(instr.group(1)), int(instr.group(2))
          if enabled:
              res += x*y

  print(res) 
    
 