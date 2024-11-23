def is_prime(num):
    # Eliminar casos triviais
    if num <= 1:  # Números menores ou iguais a 1 não são primos
        return False
    elif num == 2:  # 2 é o único número primo par
        return True
    elif num % 2 == 0:  # Números pares acima de 2 não são primos
        return False

    # Verificar divisores de 3 até a raiz quadrada de 'num'
    for i in range(3, int(num**0.5) + 1, 2):  # Apenas ímpares
        if num % i == 0:
            return False

    # Se nenhum divisor foi encontrado, é primo
    return True


def numero_primo(number):
    if number >= 1:
        for i in range(1, number):
            if number % i != 0:
                return True
            else:
                return False
                break
    elif number == 0:
        return number, 'é zero'
    else:
        return number, 'é negativo'