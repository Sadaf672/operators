# Arithmetic Operator
print(2 + 5)#Addition
print(10 - 5)#subtraction 
print(2 * 5) #multipliction 
print(10 / 5) #deivion
print(2 ** 5) #exponentiation 2*2*2*2*2
print(2 // 5) #floor_division
print(2 % 5) #modulus

# Assignment Operators
a = 30
b = 10

a *= 10
a += 10
a -= 10
a /= 10
print(a)


# Comparison Operator
num1 = 10
num2 = 20
print(num1 == num2)#false
print(num1 != num2)#true
print(num1 >= num2)#false
print(num1 <= num2)#true
print(num1 > num2)#false
print(num1 < num2)#true


#  logical Operator
#         #true     true 
print(2 == 2 and 3== 3) #True
print(2 == 2 and 3== 4) #Flase

        #or

print(2 == 2 or 5 == 3) #True
print(7 == 2 or 3 == 3) #True
          # not
print((7 == 2)) != ((3 == 3)) #True
        

#Arithmetic Operator

first_num = int(input("Enter your first number"))
second_num = int(input("Enter your second number"))
sum = first_num + second_num
print(sum)

first_num = int(input("Enter your first number"))
second_num = int(input("Enter your second number"))
sub = first_num - second_num
print(sub)

first_num = int(input("Enter your first number"))
second_num = int(input("Enter your second number"))
multi= first_num * second_num
print(multi)


first_num = int(input("Enter your first number"))
second_num = int(input("Enter your second number"))
division = first_num / second_num
print(division)

first_num = int(input("Enter your first number"))
second_num = int(input("Enter your second number"))
floor_division = first_num // second_num
print(floor_division)

first_num = int(input("Enter your first number"))
second_num = int(input("Enter your second number"))
con = first_num ** second_num
print(con)

name = "sadaf"
age = 26
is_girl =True
contact =1234
print(f"my name is {name} my age {age} ")
print(is_girl)

# membership operator

reg_user = [ "sadaf", "iqra", "saba", "sana"]
name = input("Enter your name:")

if name in reg_user:
    print("Access granted.welcome sis")
else:
    print("Access denied.you are not registered")


# identity operator
x = [1, 2, 3]
y = x

print(x is y)  # Output: True, kyunki y=x hai, dono same memory location pe hain

z = [1, 2, 3]
print(x is z)  # Output: False, kyunki x aur z alag memory locations pe hain


# Binary operator
a = 5    # Binary: 0101
b = 3    # Binary: 0011

result = a & b  # AND operation
print(result)   # Output: 1 (Binary: 0001)

