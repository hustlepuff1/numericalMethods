txt="For only {price:.2f} dollars"
print(txt.format(price=49))
txt1="I'm {fname}, {age:10d} years old".format(fname="KIM",age=33)
txt2="I'm {1:10d}, {0} years old".format("KIM2",34)
txt3="I'm {}, {:10d} years old".format("KIM3",35)
print(txt1)
print(txt2)
print(txt3)

