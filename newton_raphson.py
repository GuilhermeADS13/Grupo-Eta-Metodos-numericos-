#Implementa o newton- raphson aqui


def newton_raphson(f, f_linha, x0, eps1, eps2, kmax):
    i = x0

    if abs(f(i)) < eps1:
        return i, 0

    for k in range(1, kmax + 1):
        i_novo = i - f(i)/f_linha(i) #formula newton-raphson
        print("iteracao" , k ,"i =" , i_novo)

        if abs(f(i_novo)) < eps1 or abs(i_novo - i) < eps2:
            return i_novo, k

        i = i_novo

    return i, kmax
