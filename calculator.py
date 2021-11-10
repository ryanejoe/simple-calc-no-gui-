number_1 = int(input("enter number one:"))
number_2 = int(input("enter number two:"))
op = input("enter your operator: ")
if op =="+":
    ans= number_1 + number_2
elif op== "-" :
    ans= number_1 - number_2
elif op=="*" or op=="x":
    ans = number_1 * number_2
elif op=="/":
    ans = number_1 / number_2
else:
    print("wrong input")