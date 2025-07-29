################################################################################
#
# A regra LEGB e como o Python a usa para resolver nomes
#
# O Python segue uma ordem específica e unidirecional para busca por nomes.
# A ordem sempre vai do escopo mais interno para o mais externo:
#
# Certo ✅: Local -> Enclosing -> Global -> Built-In -> ❌ NameError
# Errado ❌: Built-In -> ❌Global -> ❌Enclosing -> ❌Local
#
# De nenhum escopo externo é possível usar algo de escopo interno.
#
################################################################################
import inspect

nome_global = "nome_global"


def func_global() -> None:
    nome_enclosing = "nome_enclosing"  # Enclosing (Local)

    def func_interna() -> None:
        print("IMPRIMINDO", nome_enclosing)

        # nome_enclosing = "CRIAR UMA NOVA VARIÁVEL NESSE ESCOPO"

        def func_mais_interna() -> None:
            nome_local = "nome_local"  # Local

            get_legb("nome_enclosing", inspect.currentframe())
            print(
                "LOCAL:",
                nome_local,
                nome_enclosing,
                "funcao_interna",
                nome_global,
                "+builtins",
            )

        func_mais_interna()

    func_interna()
    # print(
    #     "ENCLOSING:",
    #     nome_enclosing,
    #     "funcao_interna",
    #     "funcao_global",
    #     nome_global,
    #     "+builtins",
    # )


func_global()
# print("GLOBAL:", nome_global, "func_global", "+builtins")
