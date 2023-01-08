# txt = "hello world"
# print(txt.capitalize())
# import datetime
# DATE = datetime.date(year=2002,month=3,day=23)
# print(DATE)

# from decimal import Decimal

# result = Decimal('1.1') + Decimal('2.2')
# print(result)
# result2 = 1.1 + 2.7
# print(result2)

def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  fib_list = [0,1]
  for i in range(2,n+1):
    fib_list.append(fib_list[i-1] + fib_list[i-2])
  return fib_list[n]

#print(fibonacci(9999))

a = [1,2,3]
print(a[1:5])