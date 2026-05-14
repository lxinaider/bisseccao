import math


def bisseccao(f, a, b, tol=1e-8, max_iter=100):
    # Verificações
    if a >= b:
        print("O limite inferior deve ser menor que o limite superior")
        return None

    if f(a) is None or f(b) is None:
        print("Intervalo inválido.")
        return None

    if f(a) * f(b) > 0:
        print("O intervalo não contém uma raiz (f(a) e f(b) têm o mesmo sinal)")
        return None

    # Iteração
    for i in range(max_iter):
        x_m = (a + b) / 2

        print(f"i: {i}\ta: {a}\tb: {b}\tx_m: {x_m}\tf(x_m): {f(x_m)}")

        if f(x_m) == 0 or (b - a) / 2 < tol:
            return (i + 1, x_m)

        # Verifica se tá entre [a, x_m] ou [x_m, b]
        if f(a) * f(x_m) < 0:
            b = x_m
        else:
            a = x_m

    # Se passou o máximo de iterações
    print(
        "Número máximo de iterações atingido sem encontrar uma raiz dentro da tolerância"
    )
    x_m = (a + b) / 2
    return (i + 1, x_m)


def f(R):
    L = 5
    C = 1e-4
    t = 0.05
    q_0 = 0.01

    valor = (1 / (L * C)) - ((R / (2 * L)) ** 2)

    if valor < 0:
        return None

    return q_0 - math.exp(-(R * t) / (2 * L)) * math.cos(math.sqrt(valor) * t)


if __name__ == "__main__":
    # -400 e -300
    # 300 e 400
    a = int(input("Digite o limite inferior do intervalo: "))
    b = int(input("Digite o limite superior do intervalo: "))

    resultado = bisseccao(f, a, b)

    if resultado is not None:
        iteracoes, raiz = resultado
        print(f"Total de iterações: {iteracoes}")
        print(f"f(x_m) na última iteração: {f(raiz)}")
        print(f"A raiz encontrada é: {raiz}")
    else:
        print("Nenhuma raiz encontrada no intervalo especificado")
