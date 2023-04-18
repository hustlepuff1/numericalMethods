x= []
data = open('sunspots.txt','r')
for line in data:
    x.append(eval(line.split()[3]))
data.close()
print(x)
