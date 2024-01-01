# num1 = 20
# num2 = 2
# if num1 < num2: # or (num1 < num2): `:` is mandatory
#     print("num1 is less than num2")
# else: # optional
#     print("num2 is less than num1")

num1 = 200
num2 = 20
num3 = 30
if ((num1 >= num2) and (num1 >= num3)):
    print("num1 is greater")
elif ((num2 >= num1) and (num2 >= num3)):
    print("num2 is greater")
else:
    print("num3 is greater")