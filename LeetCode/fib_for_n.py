def fib(num):
 fib_list=[1,1]
 for number in range(1,num):
  current_num = fib_list[number-2]+[number-1]
  fib_list+=current_num

return fib_list[num]
