yr=[]
va=[]
finput=input('input file name?:')
data=open(finput,'r')
data.readlines(1) #head
for ln in data:
    yr.append(eval(ln.split()[0]))
    va.append(eval(ln.split()[3]))
    print(yr,va)
data.close()


fname=input('output file name?:')
f=open(fname,'w')
for k in range(0,len(yr)):
    f.write(f'{yr[k]:5d} {va[k]:15.5e}\n')
f.close()
