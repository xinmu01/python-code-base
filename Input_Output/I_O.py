f = open("test.txt",'r') 
g=open("out.txt",'w')

#print(f.read())
#print(f.read()[3])
#print(type(f.read()))
#print(next(f.readlines()))

#for line in f.readlines():
#    print(line)
    #print(1)
#    g.write(line)

print(f.readline())    
print(f.readline())  
print(f.readline())  
print(f.readline()) 
print(f.readline())   
f.close()
g.close()

