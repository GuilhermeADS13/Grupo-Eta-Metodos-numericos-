from problema import f, f_linha, eps1, eps2, kmax
import bissecao
from newton_raphson import newton_raphson
import ponto_fixo


raiz, iteracoes = newton_raphson(f, f_linha, 1, eps1, eps2, kmax)
print("Newton-Raphson: i =", raiz, "em", iteracoes, "iteracoes")
