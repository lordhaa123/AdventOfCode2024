from collections import defaultdict

if __name__ == "__main__":

  
  grid = open("input.txt",'r').read().split()
  
  grid = list(map(int, grid))
  # print(grid)

  dp = {}

  def blinkXforTsteps(x,t):
    if (x,t) in dp:
      return dp[(x,t)]
    if t == 0:
      ret = 1
    elif x == 0:
      ret = blinkXforTsteps(1,t-1)
    elif len(str(x))%2 == 0:
      temp = str(x)
      left = int(temp[:len(temp)//2])
      right = int(temp[len(temp)//2:])
      ret = blinkXforTsteps(left,t-1)+blinkXforTsteps(right,t-1)
    else:
      ret = blinkXforTsteps(x*2024,t-1)
    dp[(x,t)] = ret
    return ret
  
  print(sum(blinkXforTsteps(x,75) for x in grid))
