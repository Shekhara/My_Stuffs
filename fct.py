num = input("enter the number to find the factorial \n")

def fact(num):
    return 1 if(num == 1 or num == 0) else num * fact(num-1);

res = fact(num)

print res
