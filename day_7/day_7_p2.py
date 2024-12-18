from numpy.core.numeric import base_repr

if __name__ == "__main__":

  grid = []
  for line in open("input.txt",'r').readlines():
    # print(line.split())
    grid.append(line.split())
  
  for i in grid:
    i[0] = i[0][:-1]
  
  grid = [[int(num) for num in row] for row in grid]
  
  def increment_base3_string(base3_str):
    incremented = ""
    try:
        incremented = base_repr(int(base3_str, 3) + 1, 3)
    except:
        print("Can't parse input")
    return incremented.zfill(len(base3_str))
  
  def getRes(ops,nums):
    temp = nums[0]
    for i in range(len(ops)):
      if ops[i] == '0':
        temp = temp + nums[i+1]
      elif ops[i] == '1':
        temp = temp * nums[i+1]
      else:
        temp = int(str(temp)+str(nums[i+1]))
      # print(ops,temp)
    return temp
  
  res = 0
  for row in grid:
    ans = row[0]
    nums = row[1:]
    ops = '0' * (len(nums)-1)
    for i in range(3**len(ops)):
      if getRes(ops,nums) == ans:
        res += ans
        break
      ops = increment_base3_string(ops)
      # print(ops)
      
  print(res)
