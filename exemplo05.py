################################################################################
#
# Relação entre escopo e namespace
#
# Escopo e namespace são assuntos interligados e muitas vezes confundidos.
# Mas a diferença entre eles é simples:
#
# - Escopo define os limites e o tempo de vida de um trecho de código que tem
#   um namespace.
# - Namespace é um objeto real que guarda os nomes e seus respectivos valores.
#
# É por isso que, ao fazer `import x`, dizemos que `x` é um namespace, ele
# guarda nomes como `x.func_global()`, `x.valor`, etc.
#
################################################################################
import x


def func_global() -> None:
    print(f"Estou em: {__name__} - {__file__.split('/')[-1]}")


x.func_global()
func_global()
print()
print(globals())
