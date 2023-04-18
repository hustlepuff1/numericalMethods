x=[]
y=[]
data=open('dae11.txt','r')
data.readlines(1)
for ln in data:
    x.append(eval(ln.split()[0]))
    y.append(eval(ln.split()[1]))
    print('x=',x[len(x)-1],' y=',y[len(y)-1])
    #print('x={:012.3e}'.format(x[len(x)-1]),' y=', y[len(y)-1])
data.close()
print(x)
print(y)
