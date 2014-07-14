print range(3)
for x in range(3):
    print 'x=',x
    
names = [['dave', 'jeff', 'noel'],['mark',True,21],['mike', 14, False]]
for x in names:
    print x
print names[1][1]



y = list()
for x in range(3):
    y.append(x**2)
print y
# notes are made by preceding with a hashtag

x = range(4)
y = [i**2 for i in x]
print y

y = [i+3 for i in y]
print y

