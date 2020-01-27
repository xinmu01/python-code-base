f = open("test.txt",'r') 
g = open("out.txt",'w')

for line in f.readlines():
    print(line.strip())
    g.write(line)

   
f.close()
g.close()

