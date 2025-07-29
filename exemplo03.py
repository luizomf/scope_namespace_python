################################################################################
#
# O que é namespace?
#
# Namespace é uma estrutura de dados real que mapeia nomes para objetos. Cada
# chave é o nome que você define e o valor é o objeto correspondente no seu
# código. Sempre que você cria um nome, essa associação é guardada dentro de um
# namespace.
#
# Vamos usar `globals()` e `locals()` no mesmo código anterior e confirmar isso.
#
# globals(): Retorna um dicionário que representa o namespace global do módulo
#            atual. Isso inclui todos os nomes definidos na raiz do arquivo.
# locals():  Retorna um dicionário com os nomes definidos no escopo local onde
#            a função está sendo executada. Importante: ela só inclui nomes que
#            já foram definidos antes da sua chamada.
#
################################################################################

namespace_global = globals()
um_nome = "um_nome (GLOBAL)"

# # print(id(um_nome), id(namespace_global["um_nome"]))
# print(dir(__builtins__))


def func_global(sou_local: str) -> None:
    um_nome = "um_nome (LOCAL)"
    outro_nome = "outro_nome (LOCAL)"
    print("LOCALS (namespace da função)")
    print(locals())
    print()


# func_global("arg (local)")
# print()

# print("GLOBALS (namespace do módulo)")
# print(globals())

#
#
#
#
#
