#taking input
first_number = input("ENTER YOUR FIRST NUMBER:")
action= input("ENTER YOUR ACTION(+,-,*,/):")
second_number = input("ENTER YOUR SECOND NUMBER:")

try:
    first_number=float(first_number)
    second_number=float(second_number)
except:
    print("invalid input")
    quit()
if action == '+':
    print(first_number+second_number)
elif action == '-':
    print(first_number-second_number)
elif action == '/':
     print(first_number/second_number)
elif action == '*':
    print(first_number*second_number)
else :
    print('invalid action')
quit()