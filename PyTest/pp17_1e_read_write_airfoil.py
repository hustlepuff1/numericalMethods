x=[]
y=[]
finput=input('airfoil file name?:')
data=open(finput,'r')
data.readlines(1)
for ln in data:
    x.append(eval(ln.split()[0]))
    y.append(eval(ln.split()[1]))
data.close()


fname=input('output filename?:')
f=open(fname,'w')
for k in range(0,len(x)):
    f.write(f'{x[k]:15.5e} {y[k]:15.5e}\n')
f.close()
