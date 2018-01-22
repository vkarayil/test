class myclass:
    ''' doc string for myclass '''
    a = 10

    def __init__(self,r=11,i=12):
        self.real = r
        self.imag = i

    def getdata(self):
        print("{0}+{1}j".format(self.real,self.imag))
        
    def func(self):
        print("inside class method func")

c1 = myclass(2,3)
c2 = myclass(20,30)
c3 = myclass()

print(c1.a,c1.real,c1.imag)
c1.getdata()
c2.getdata()
c2.attr = 100
print(c2.attr,c2.real,c2.imag)
print(c3.real,c3.imag)
c3.value= 200
print(c3.value,c3.real,c3.imag)
c3.a = 2000
print(c1.a,c2.a,c3.a)

print(c1.a)
#del c1.a
del c2.attr
#print(c2.attr)
del myclass.func
#c2.getdata()
#c2.func()
del c1
del c2
del c3
print(c1.a,c2.real,c3.imag)


