def fib_linear(n):
    try:
        n = int(n)
    except:
        print("Insira um número inteiro.")
        return
    
    if n < 0:
        print('Insira um valor positivo.')
        return

    if n == 0:
        return 0
    
    anterior, atual = 0, 1
    for _ in range(2, n + 1):
        a_temp = atual
        atual = atual + anterior
        anterior = a_temp

    return atual