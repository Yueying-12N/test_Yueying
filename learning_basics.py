print('Bonjour')

mon_num = 'Yueying'
print(mon_num)

#list
a = [1,2,4]
b = a
b.append(8)
print(b)

#dict
scores={'L':'98','M':'99'}
print(scores,type(scores))

#former value will be covered
a = 23
a = 'asd'
print(a)

#class
class BlackPink:
    b = 0.0
    c = 1.0

a = BlackPink
print(a.b)
print(a.c)

a.Beu='Jisoo'
print(a.Beu)

#using logical operation must be the same type
#BP = 'BlackPink'
#BP = BP + 10;

#Types
from fractions import Fraction
a = None
b = False
c = 9
d = 3.1415926
e = Fraction(3,12)  #Fraction(a,b) = a/b, and it will simplified
f = 'Croissant'
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
print(f,type(f))

#bin() returns the binary representation of an integer int or long int.
print(bin(3))
print(bin(15))
print(bin(2**5))  # ** is equal to ^ in C

#tuple list dict
g = [3,1,4,1,5,9]  #list
h = (2,6,5,3,5,8,9)  #tuple
i = {'k1':1, 'k2':2, 'k3':3}
print(g,type(g),'\n',h,type(h),'\n',i,type(i),'\n')
print(i['k1'],i['k2'],i['k3'])

#None type
from math import sqrt

def simple_sqrt(n):  # remind the ':'
    if n < 0:
        return None
    else:
        return sqrt(n)


s = simple_sqrt(4)
print(s)

#Numeric operations
print(3**2)
print(11%2)
print(11//2)

greeting = 'Bonjour, ' + "ca va?" # single or double quotes
print(greeting)

# Tuple
a = 11
b = 22
a,b = b,a
print(a,b)
a,(b,c,d) = 3,(4,5,(7,8,9))
print(d)
print(d[2])
t = 'Hello', 'Python', 90
print(t,type(t))

org = 1, 'string', (), tuple()

def fun_3(number,string,first_tuple,second_tuple):
    return(number,string,first_tuple)

a,b,c = fun_3(*org)  # ‘*’will unpack the set of org
print('a=',a,', b=',b,',c=',c)

#List
a = 'from'
def country():
    return('Spain')
lst = ['Halo',a,country()]
print(lst,'\n','length of the list is',len(lst))
print('Spain' in lst)
print('The country is ',lst[2])

#sort and copy
a = [1,5,23]+[2,65,34]
b = a
c = a.copy()
a.sort()
print(b)
print(c)

#Slicing
asd = [1,2,3,4,5,6,7]
print(asd[:5:])
asd[3:4]='string'
print(asd)  #mixed type
print(asd[::-1])

#Dictionaries
wer = {'as':1,'tesr':343}
wer[(1,2)]=90
# wer[(1,[3])]=374   the key can not be list
print(wer.items())

# The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1
# respectively, in almost all contexts, the exception being that when converted to a string
# the strings ‘False’ or ‘True’ are returned, respectively
cra = {1:90,(3,4,7):{'crazy':666}}
print(cra[(3,4,7)])
ano = {True:'right',1:'yes',1.0:'no'}
print(ano[True],'\n',ano[1],'\n',ano[1.0])
