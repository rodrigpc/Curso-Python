def fib(n):    # escrever séries de Fibonacci até n
     """Imprima uma série de Fibonacci até n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()

# Agora chame a função que acabamos de definir:
fib(2000)