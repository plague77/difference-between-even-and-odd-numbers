print ("enter 'x' to exit");
num = input("enter num");
if num =='x':
    exit();
try:
    number = float(num);
except ValueError:
    print("please enter num");
else:
    check = number%2;
    if check ==0:
        print(int(number), "this is a even num");
    elif check==1:
        print(int(number), "this is an odd num");
    else:
        print(number, "def is not a num");