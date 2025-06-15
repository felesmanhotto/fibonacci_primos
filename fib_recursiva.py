def fib_recursiva(n):
    try:
        n = int(n)
    except:
        return "Insira um número inteiro."
    
    if n < 0:
        return 'Insira um valor positivo.'
    
    if n == 0:      # casos base para finalizar a recursão
        return 0
    if n == 1:
        return 1
    n = fib_recursiva(n-1) + fib_recursiva(n-2)

    return n


testes = [-1, 0, 1, 4, 6, 'a']
for valor in testes:
    print("Entrada: ", valor,'\n', "Saída: ", fib_recursiva(valor))
    print()