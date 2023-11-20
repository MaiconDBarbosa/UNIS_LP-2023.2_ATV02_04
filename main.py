def eh_primo(numero):
    # Verifica se o número é menor que 2 (números negativos e 1 não são primos)
    if numero < 2:
        return False

    # Verifica se o número é divisível por algum número de 2 até a raiz quadrada do número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True

def testar_primos_1_a_100():
    for i in range(1, 101):
        if eh_primo(i):
            print(f"{i} é primo.")
        else:
            print(f"{i} não é primo.")

if __name__ == "__main__":
    testar_primos_1_a_100()
