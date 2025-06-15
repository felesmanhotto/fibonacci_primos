import math as m

def p_linear(n):
    try:
        n = int(n)
    except:
        return "Insira um número inteiro."
    
    if n < 2:
        return 'Insira um valor maior que 1.'
    
    primos = []
    for i in range(2, n+1):
        is_primo = True

        for j in range(2, int(m.sqrt(i)) + 1):  # para um valor maior que a raiz quadrada de um numero ser seu divisor, deveria 
            if i % j == 0:                      # multiplicar um valor menor que a raiz quadrada, os quais ja foram verificados
                is_primo = False
                break

        if is_primo:
            primos.append(i)

    return primos


testes = [0, 1, 2, 5, 10, 'a']
for valor in testes:
    print("Entrada: ", valor,'\n', "Saída: ", p_linear(valor))
    print()