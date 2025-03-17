from collections import defaultdict
import re
import z3

if __name__ == "__main__":

  
  grid = open("input.txt",'r').read().strip()
  def ints(s):
    return [int(x) for x in re.findall('\d+', s)]
  
  queries = grid.split("\n\n")
  # print(queries)
  
  def solve(ax,ay,bx,by,px,py):
    
    px += 10000000000000
    py += 10000000000000
    
    t1 = z3.Int('t1')
    t2 = z3.Int('t2')
    sol = z3.Solver()
    
    sol.add(t1>0)
    sol.add(t2>0)
    
    sol.add(t1*ax + t2*bx == px)
    sol.add(t1*ay + t2*by == py)
    
    if sol.check() == z3.sat:
      return sol.model().eval(3*t1+t2).as_long()
    else:
      return 0
  
  ans = 0
  for query in queries:
    temp = ints(query)
    ans += solve(*temp)
  print(ans)
    
