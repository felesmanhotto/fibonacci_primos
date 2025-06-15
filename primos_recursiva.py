import math as m

def p_recursiva(n, primos=[]):  # a primeira chamada cria a lista vazia

    try:
        n = int(n)
    except:
        print("Insira um número inteiro.")
        return
    
    if n < 2:
        primos.reverse()
        return primos

    is_primo = True
    for i in range (2, int(m.sqrt(n)) + 1):
        if n % i == 0:
            is_primo = False
            break

    if is_primo:
        primos.append(n)
    
    return p_recursiva(n-1, primos) # outras chamadas usam a lista atualizada