def fib(n): 
    if (n == 1) or (n == 2): 
        return 1 
    else: 
        return fib(n-2) + fib(n-1)

termo_fib = 6
print(f'O {termo_fib}º termo da sequência de Fibonacci é: {fib(termo_fib)}') 