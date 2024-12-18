if __name__ == "__main__":

  grid = []
  for line in open("input.txt",'r').readlines():
    # print(line.split())
    grid.append(line.split())
  
  for i in grid:
    i[0] = i[0][:-1]
  
  grid = [[int(num) for num in row] for row in grid]
  
  def increment_binary_string(binary_str):
      incremented = bin(int(binary_str, 2) + 1)[2:]
      return incremented.zfill(len(binary_str))
  
  def getRes(ops,nums):
    temp = nums[0]
    for i in range(len(ops)):
      if ops[i] == '0':
        temp = temp + nums[i+1]
      else:
        temp = temp * nums[i+1]
      # print(ops,temp)
    return temp
  
  res = 0
  for row in grid:
    ans = row[0]
    nums = row[1:]
    ops = '0' * (len(nums)-1)
    for i in range(2**len(ops)):
      if getRes(ops,nums) == ans:
        res += ans
        break
      ops = increment_binary_string(ops)
      
  print(res)
