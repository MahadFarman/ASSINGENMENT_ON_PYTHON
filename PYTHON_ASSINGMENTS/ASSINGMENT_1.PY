# 1. Print Your Name with your Father name and Date of birth using suitable escape sequence character

print("Name:\tMahad\nF/Name:\tFarman\nDate_Of_Birth:\t6-5-2010")

# 2. Write your small bio using variables and print it using print function
name="Mahad Farman"
age = '16'
city="karachi"
hobby="Programming"

print(f'My name is {name}\nI am {age} years old\nI am living in {city}\nMy hobby is {hobby}')

# 3. Write a program in which use all the operators we can use in Python
# Arithmetic Operators
a =int(input("Enter the number :"))
b =int(input("Enter the number :"))

print(f"addition {a + b} ")
print(f"subraction {a - b} ")
print(f"multiplication {a * b} ")
print(f"division {a / b} ")
print(f"floor division {a // b} ")
print(f"modulus {a % b} ")
print(f"exponantation {a ** b} ")

# Comparison Operators
a =int(input("Enter the number :"))
b =int(input("Enter the number :"))
print(a==b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)

# Assignment Operators
a =int(input("Enter the number :"))
b =int(input("Enter the number you add :"))
a+=b
print(a)

a =int(input("Enter the number :"))
b =int(input("Enter the number you sub :"))
a-=b
print(a)

a =int(input("Enter the number :"))
b =int(input("Enter the number you mul :"))
a*=b
print(a)

a =int(input("Enter the number :"))
b =int(input("Enter the number you divide :"))
a/=b
print(a)

# Logical Operators
a =int(input("Enter the number :"))
b =int(input("Enter the number :"))
print("AND :-", a>b and a==b)
print("OR :-", a<b or a==b)
print("NOT :-", a==b or a>b)

# Bitwise Operators
a =int(input("Enter the number :"))
b =int(input("Enter the number :"))
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

4. Mention Marks of English, Islamiat and Maths out of 100 and Calculate Percentage
Marks_1=int(input("Enter the marks of English :"))
Marks_2=int(input("Enter the marks of Islamiat :"))
Marks_3=int(input("Enter the marks of Maths :"))

Total_Marks=300
Obtained_Marks=(Marks_1+Marks_2+Marks_3)
Percentage=round((Obtained_Marks/Total_Marks)*100, 2)

print("Total_Marks", Total_Marks)
print("Obtained_Marks",Obtained_Marks)
print("Your Percentage",Percentage,"%")

# 5. Swap the values of a and b without using a third variable
a=int(input("enter the number 1 :"))
b=int(input("enter the number 2 :"))

print("Before Swapping,")
print(f'a= {a}')
print(f'b= {b}')

print("After Swapping")
print(f'a= {b}')
print(f"b= {a}")

# 6. Calculate Area and Circumference of a Circle
radius=float(input("enter the radius of circle :"))
PI= 3.14
Area= PI*radius*radius
Circumference= 2*PI*radius

print(f"the radius of circle is :{radius} ")
print(f"the Area of circle is :{Area}")
print(f"the Circumference of circle is :{Circumference}")

# 7. Calculate Discount Amount and Final Price
Product_price=int(input("Enter the Price :"))
Discount_percentage=int(input("Enter the Discount_percentage :"))
Discount_price=(Product_price*Discount_percentage)/100
Final_price= Product_price - Discount_price

print(f"The Product_price is {Product_price}")
print(f"The Discount_price is {Discount_price}")
print(f"The Final_price is {Final_price}")

