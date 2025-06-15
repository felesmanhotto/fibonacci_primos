def fib_recursiva(n):
    try:
        n = int(n)
    except:
        print("Insira um número inteiro.")
        return
    
    if n < 0:
        print('Insira um valor positivo.')
        return
    
    if n == 0:      # casos base para finalizar a recursão
        return 0
    if n == 1:
        return 1
    n = fib_recursiva(n-1) + fib_recursiva(n-2)

    return n