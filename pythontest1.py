print("Hello World")
date="1.25.2019"
x =9 + 15 
print(date)
print(x)

import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0,2 * np.pi, 1000)
y = np.sin (x)
plt.plot (x, np.sin(x))
plt.show()


#%% 
print ("print text")
a, b, c = 1, 2, 3
print (a,b,c)
my_string = "string"
print (my_string)
flag_1 = True
flag_2 = False 
my_variable = None

# upper and lower case matters
"""
this is the description
"""
aA=3
Aa=2
print (aA,Aa)

c = a/b
d = b/a
print (c,d)

#%%
a,b=3,2
print (type(a))
print (a/b)
a=2.
print (type(a))
a += 3
print (a)
a-=2 
print (a)
a *= 3
print (a)
a /= 2.5
print (a)

#%% 
# get the 整除，余数
a=10.5//3
print (a)
a = 11 % 3
print (a)

#%%
a,b =3,2
print (a<=b)
print (b == min(a,b))
print (2 == 2.)
a=(not(2>3)&(4>3))
print (a)

#%%
a = 3
if a<1:
    print ("a<1")
elif a<10:
    print ("1<a<10")
else: 
    print ("nothing")


a = 3.6
if a > 0:
    if a % 1 == 0:
        print ('a是正整数')
    else:
        print ('a是正小数')
elif a < 0:
    if a % 1 == 0:
        print ('a是负整数')
    else:
        print ('a是负小数')
else:
    print ('a是0')


#%%
for i in range (5):
    print ("show it 5 times")
for i in range (5):
    print ("This is the", str(i+1), "time")
#%%
a=1
while a<5:
    a+=1
print (a)

a=1
while a<10:
    a+=1
else:
    print (a)

a = 1
for i in range(10000):
    a += 1
    if a >= 100:
        break
print (a)

#%%
# function
def myf(a):
    print ("The input number is", str(a))
myf(4)

def myf(a):
    result = a + 1
    return result
print (myf(4))
b= myf(3.5)
print (b)

def add(a,b):
    return a + b 
print (add(3.5, 4.1))



#%%
# 递归:斐波那契数
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n >= 3:
        return fibo(n-1) + fibo(n-2)

print (fibo(8))

def add(a, b):
    return a + b
def square_sum(a, b):
    return add(a, b) ** 2
print (square_sum(2, 3))

#%%
def third_side(a, b):
    if a<=0 or b<=0 :
        return 0
    else :
        return (a**2+b**2)**0.5
print (third_side(3,4))
print (third_side(4,0))