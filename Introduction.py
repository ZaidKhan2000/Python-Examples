'''To check the python version you are using
    python --version
'''

'''Addition'''
print(3+4)
'''Subtraction'''
print(3-4)
'''Multiplication'''
print(3*4)
'''Division'''
print(3/4)
'''Exponential'''
print(3**4)
'''Modulus'''
print(3%4)
'''Quotient'''
print(3//4)

'''To check the data types'''
print(type(10))
print(type(10.23))
print(type("Hello There"))
print(type(10+6j))


'''l=[]
for n in range(2000,3201):
    if n%7==0 and n%5!=0:
        l.append(n)
    
print(l)   

for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")

fact=1
n=int(input("Enter the number:"))
for i in range(1,n+1):
    fact=fact*i

print(fact)


a=[1,2,3,4]
try:
    print(a[10])
except Exception as s:
    print("Hello",s)
'''

'''Data Types Examples'''
#Integer:10,20,21,13214
#Float:3.14,27.189,678.98
#Complex:32+22j,12-14j
#String:'a','Hi there',"Hello My name is Zaid!"
#Boolean:is 2>3-->False,is 50*6==300-->True
#List:[1,3,3.14,32+22j,'Hi',"Hello"b]
#Tuple:(1,3.2,'hi')-->They Are Immutable(Cannot be modified once created)
#Set:{1,2.4,'Hello'}-->Same logic as Set in maths
#Dictionary:{'Name':'Dean','Age':37}

#Find an Euclidian distance between (2, 3) and (10, 8)
a1,a2,b1,b2=2,3,10,8
Euclidian_distance=(((b1-a1)**2)+((b2-a2)**2))**(1/2)
print("Euclidian distance is:",Euclidian_distance)

