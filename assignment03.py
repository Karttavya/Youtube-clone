name = input("Enter your name: ")
print("Aur" ,name,", kya haal chal!")

num1=int(input("\nenter number one:"))
num2=int(input("enter number two:"))

operation=int(input('''
Whaat do you want me to do
1. Addition
2. subtraction
3. multiplication
4. division
reply (1,2,3 or 4):'''))

if operation==1:
    print("Addition:",num1+num2)
elif operation==2:
    print("Subtraction:",num1-num2)
elif operation==3:
    print("Multiplication:",num1*num2)
elif operation==4:
    print("Division:",num1/num2)
else:
    print("\nAUUKAAAT ME")
