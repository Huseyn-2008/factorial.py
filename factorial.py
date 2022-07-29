number = 10
def factorial(i):
     if i == 0:
          return 1
     l = 1
     h = 0

     while h < i:
          h += 1
          l = l * h
     return l
print("Factorial of number {i} equals to {l}".format(i = number, l = factorial(number)))
