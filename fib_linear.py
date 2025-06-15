def fib_linear(n):
    try:
        n = int(n)
    except:
        return "Insira um número inteiro."
    
    if n < 0:
        return 'Insira um valor positivo.'

    if n == 0:
        return 0
    
    anterior, atual = 0, 1
    for _ in range(2, n + 1):
        a_temp = atual
        atual = atual + anterior
        anterior = a_temp

    return atual


testes = [-1, 0, 1, 4, 6, 'a']
for valor in testes:
    print("Entrada: ", valor,'\n', "Saída: ", fib_linear(valor))
    print()