a = 1
b = 2
print('a = {}, b = {:>6}'.format(a, b))
print('a = %d, b = %6.2f' % (a, b))
print(f'a = {a}, b = {b:^^6}')

name1 = 'Kim'
name2 = 'Jin'

print('%s likes %s so much.' % (name1, name2))
print(f'{name1} likes {name2} much more about {b:0<3}%')
print('{} asked {} to marry her on {:1<2}th of {:0>2}st.'.format(name2, name1, a, b))
print('there are %6.7d apples' % (a))
print(f'{name2} asked {name1} to marry her on {b:1>2}nd of {a:0<2}th')
