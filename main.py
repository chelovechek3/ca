"""s = input("Введите текст:")
a = 0
vowels = set("аеияо")
for letter in s:
    if letter in vowels:
        a += 1
print("Количество гласных:")
print(a)"""
"""d =  int(input("Введите первое число: "))
x= input("Введите оператор действия: ")
f =  int(input("Введите второе число: "))
def myfunc ():
 print(d + f)
def myfunc1 ():
 print(d-f)
def myfunc2():
 print(d*f)
def myfunc3():
    print(d**f)
def myfunc4():
    print(d//f)
def myfunc5():
 print(d%f)
def myfunc6():
    print(d/f)
if x=="+":
     myfunc()
elif x=="-":
    myfunc1()
elif x=="*":
    myfunc2()
elif x=="**":
 myfunc3()
elif x=="//" and f!=0:
    myfunc4()
elif x =="%" and f!=0:
    myfunc5()
elif x =="/" and f!=0:
    myfunc6()
else: print("Вы совершили ошибку в введении данных"""
"""import random
def myfunc1():
 q = []
 for i in range(3) :
  l=(random.randint(1,250))
  j=(random.randint(1,250))
  o=(random.randint(1,250))
  h = [l,j,o]
  for n in h:
   q.append('.')
  print(h)
  print(q)"""
"""def bank(K,N,L):
 T = int(input("Введите количество процентов: "))
 S = int(input("Введите количество денег: "))
 E= int(input("Введите количество лет, на которое хотите сделать вклад: "))
 X = (S*T)/100
 d=S+E*X
 c=(K*L)/100
 q=K+N*c
 print("Через",E,"лет у вас будет",d,"денег")
 for i in range (E):
    S+=X
    a=S*T/100
    z=a+T
    p=(((S+a)*T)/100)
    print(z+S)
 #print('Под',L,'%',"годовых")
 return q
bank(1000,20,3)"""
#Дз на 27.12:
"""import time
def calculate_time(func):
    def funcc(a):
        t = time.time()
        funccc = func(a)
        t1 = time.time()
        return funcc, print(round(t1-t,2))
    return funcc
@calculate_time
def some_function(numbers):
    my_list1 =[]
    for i in range(1, numbers +1):
        str_numbers = str(i)
        my_list1.append(i)
some_function(int(input()))"""
#Дз на 31.12.2023:
with open('d.txt', 'r') as input_file, open('X.txt', 'w') as output_file:
    for line in input_file:
        parts = line.strip().split(':')
        output_file.write(':'.join(parts[:2]) + '\n')



