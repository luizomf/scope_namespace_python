"""Um módulo de exemplo"""

################################################################################
#
# O que é escopo
#
# Escopo é a região do código onde um nome está diretamente acessível.
# Ele determina os limites e o tempo de vida dos nomes definidos internamente.
#
# Escopo é usado para encapsular o código e evitar colisões de nomes e efeitos
# colaterais indesejados.
#
# O Python tem quatro tipos de escopos: Built-In, Global, Enclosing e Local.
# Esses escopos são dinâmicos. O interpretador pode criar e apagar em tempo de
# execução.
#
# Cada escopo tem seu "espaço de nomes" (namespace), que é um local onde os
# nomes e seus respectivos objetos são armazenados.
#
################################################################################

# nome definido no escopo global (módulo)
um_nome = "um_nome (GLOBAL)"


# nome definido no escopo global (módulo)
def func_global(sou_local: str) -> None:
    # Escopo local (função e seus parâmetros)

    # `um_nome` no escopo local é OUTRA VARIÁVEL (sem relação outro escopo)
    um_nome = "um_nome (LOCAL)"  # nome definido no escopo local
    outro_nome = "outro_nome (LOCAL)"  # nome definido no escopo local

    # Parâmetros de funções também são do escopo local da função
    print(f"Dentro da função: {um_nome}, {outro_nome}, {sou_local}")


# ISSO NÃO FUNCIONA
# print(outro_nome, sou_local)

# Isso é injetado automaticamente pelo Python no escopo global
print("Nome do módulo:", __name__)
print("Arquivo do módulo:", __file__)
print("Documentação do módulo:", __doc__)
print()  # apenas uma quebra de linha

func_global("arg (local)")
# Saída - Dentro da função: um_nome (LOCAL), outro_nome (LOCAL), arg (local)

print(f"Fora da função: {um_nome}")  # Acessa a variável GLOBAL
# Saída - Fora da função: um_nome (GLOBAL)


#
#
#
#
#
