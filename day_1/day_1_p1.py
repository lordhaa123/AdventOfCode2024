  
if __name__ == "__main__":
  
    a,b = [],[]
    for line in open("input.txt",'r').readlines():
        # print(line.split())
        line = line.split()
        a.append(int(line[0]))
        b.append(int(line[-1]))
        
    a.sort()
    b.sort()
    
    res = 0
    
    for i in range(len(a)):
      res += (abs(a[i]-b[i]))
    
    print(res)
    


    