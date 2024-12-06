from collections import defaultdict , deque

if __name__ == "__main__":
  
  grid = []
  rules = []
  pages = []
  change = 0
  for line in open("input.txt",'r').readlines():
    # print(line.split())
    grid.append(line.split())
    if grid[-1] == []:
      change = 1
      continue
    
    if change == 0:
      tmp = line.split()[0].split('|')
      temp = [int(tmp[0]),int(tmp[-1])]
      rules.append(temp)
    else:
      tmp = line.split()[0].split(',')
      temp = list(map(int,tmp))
      pages.append(temp)
  
  rules_mp = defaultdict(set)
  rules_mp_rev = defaultdict(set)
  
  for rule in rules:
    rules_mp[rule[1]].add(rule[0])
    rules_mp_rev[rule[0]].add(rule[1])
    
  res = 0
  for page in pages:
    
    ok = True
    for i,x in enumerate(page):
      for j,y in enumerate(page):
        if i<j and y in rules_mp[x]:
          ok = False

    if not ok:
      correct = []
      Que = deque([])
      temp = {i:len(rules_mp[i] & set(page)) for i in page}
      for i in page:
        if temp[i] == 0:
          Que.append(i)
      
      while(Que):
        x = Que.popleft()
        correct.append(x)
        
        for y in rules_mp_rev[x]:
          if y in temp:
            temp[y] -= 1
            if temp[y] == 0:
              Que.append(y)
      
      res += correct[len(correct)//2]
    
  print(res)
  
  