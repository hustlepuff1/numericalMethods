f = open('testfile.txt','w')
for k in range(101,105):
    f.write(f'{k:4d} {k**2:6d} \n')
    #f.write('\n')
f.close()
