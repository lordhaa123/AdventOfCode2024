from collections import defaultdict

if __name__ == "__main__":

    a,b = [],[]
    for line in open("input.txt",'r').readlines():
        # print(line.split())
        line = line.split()
        a.append(int(line[0]))
        b.append(int(line[-1]))
    
    mp = defaultdict(lambda: 0)
    
    for i in b:
      mp[i] += 1
      
    res = 0
    
    for i in a:
      res += i*mp[i]
      
    print(res)
        
    