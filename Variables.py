#Day2:30 Days of python programming
first_name='Zaid'
last_name='Khan'
full_name='Zaid Khan'
country='India'
city='Mumbai'
age=23
year=2024
is_married=False
is_true=True
is_light_on=False
a,b,c,d=1,2,3,4

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#Using the len() built-in function, find the length of your first name
print(len(first_name))

#Compare the length of your first name and your last name
a=len(first_name)
b=len(last_name)
print(a==b)

'''Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
'''
num_one=5
num_two=6
variable_total=num_one+num_two
variable_diff=num_one-num_two
variable_product=num_one*num_two
variable_division=num_one/num_two
variable_remainder=num_one%num_two
variable_exp=num_one**num_two
variable_floor_division=num_one//num_two

'''The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
'''
radius=30
area_of_circle=3.14*radius**2
circum_of_circle=2*3.14*radius

#Take radius as user input and calculate the area.
radius2=int(input("Enter the radius of a circle:"))
area_of_Usercircle=3.14*radius2**2

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
User_first_name=input("Enter your first name:")
User_last_name=input("Enter your last name:")
User_country=input("Enter your country:")
User_age=int(input("Enter your age:"))
print("Hi,my name is",User_first_name,User_last_name,"\nI live in",User_country,"and my age is",User_age)