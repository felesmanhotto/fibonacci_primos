import math as m

def p_recursiva(n, primos=None):  # a primeira chamada vai criar a lista na variavel primos

    try:
        n = int(n)
    except:
        return "Insira um número inteiro."
    
    if n < 2:
        if not primos:
            return 'Insira um valor maior que 1.'
        primos.reverse()
        return primos
    
    if not primos:
        primos = []

    is_primo = True
    for i in range (2, int(m.sqrt(n)) + 1):
        if n % i == 0:
            is_primo = False
            break

    if is_primo:
        primos.append(n)
    
    return p_recursiva(n-1, primos) # outras chamadas usam a lista atualizada


testes = [0, 1, 2, 5, 10, 'a']
for valor in testes:
    print("Entrada: ", valor,'\n', "Saída: ", p_recursiva(valor))
    print()