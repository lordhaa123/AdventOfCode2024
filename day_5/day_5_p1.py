from collections import defaultdict

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
  
  # print(rules)
  # print(pages)
  
  rules_mp = defaultdict(set)
  
  for rule in rules:
    rules_mp[rule[1]].add(rule[0])
    
  res = 0
  for page in pages:
    
    ok = True
    for i,x in enumerate(page):
      for j,y in enumerate(page):
        if i<j and y in rules_mp[x]:
          ok = False
    if ok:
      res += page[len(page)//2]
    
  print(res)
  
  