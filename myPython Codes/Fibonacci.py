def fib(n):
    fibo_list = [0,1]
    for i in range (2,n):
        new_value = fibo_list[i-1] +fibo_list[i-2]
        fibo_list.append(new_value)
    return fibo_list
        
def get_input():
    ret_val = 0
    s = input('Enter the length of the Fibonacci sequence: ')
    if s.isdigit():
        if int(s) > 2:
            ret_val = int(s)
        else:
            print("Please input a number larger than 2.")
    return ret_val
    

s = 0
while s == 0:
    s = get_input()
for num in fib(s):
    print(num)
