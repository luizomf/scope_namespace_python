################################################################################
#
# o que é namespace?
#
# namespace é uma estrutura de dados real que mapeia nomes para objetos. cada
# chave é o nome que você define e o valor é o objeto correspondente no seu
# código. sempre que você cria um nome, essa associação é guardada dentro de um
# namespace.
#
# vamos usar `vars()` e `dir()` no mesmo código anterior e confirmar isso.
#
# `vars()`: retorna o atributo `__dict__` de um objeto, que é onde seus
#           atributos são armazenados. se chamada sem argumentos, `vars()` se
#           comporta exatamente como `locals()`, retornando o namespace local.
# `dir()`:  sem argumentos, `dir()` lista todos os nomes disponíveis no escopo
#           atual. com um objeto como argumento, tenta listar todos os nomes
#           acessíveis nele (como métodos e atributos). note que `dir()`
#           retorna apenas os nomes, não os objetos ou seus valores.
#
################################################################################

um_nome = "um_nome (global)"


def func_global(sou_local: str) -> None:
    um_nome = "um_nome (local)"
    outro_nome = "outro_nome (local)"
    print("locals (namespace da função)")
    print("dir", dir())
    print("vars", vars())
    print()


# func_global("arg (local)")
# print()

print("globals (namespace do módulo)")
print("dir", dir())
print("vars", vars())

#
#
#
#
#
