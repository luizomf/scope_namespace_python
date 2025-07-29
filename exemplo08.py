################################################################################
#
# PARA NERDS: varnames, freevars, cellvars
#
# Em alguns momentos você pode ver um comportamento estranho ao solicitar o
# namespace local de uma função. Ao LER uma variável do enclosing, ela pode
# aparecer como parte do namespace local (da a impressão que ela foi definida
# internamente na função). O que é isso?
#
# Detalhe: isso pode mudar dependendo do interpretador que você usar.
#
# ** Freevars são as variáveis da função externa que estão sendo usadas dentro
#    da função interna. A gente detecta isso pela função interna, porque ela é
#    quem depende desses nomes. Eles entram em co_freevars.
# ** Cellvars são as variáveis declaradas na função atual (externa) que
#    precisam ser capturadas porque são usadas por funções internas. A gente
#    detecta isso pela função externa, porque ela é quem fornece essas
#    variáveis pro closure. Eles aparecem em co_cellvars.
# ** Varnames são as variáveis locais de verdade, exclusivas da função. Elas
#    estão em co_varnames e não fazem parte de nenhum closure, só existem ali
#    dentro mesmo.
#
#
################################################################################


nome_global = "nome_global"


def func_global() -> None:
    nome_enclosing = nome_global

    def func_interna() -> None:
        nome_local = nome_enclosing

        print("dir/locals func_interna: ", f"[color(45)]{', '.join(dir())}")
        get_all_names(func_interna.__code__)

    func_interna()
    print("dir/locals de func_global: ", f"[color(45)]{', '.join(dir())}")
    get_all_names(func_global.__code__)


func_global()
