def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
term=int(input("enter number of terms: "))
for i in range(term):
    print(fib(i), end=" ")    
