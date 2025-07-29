# ruff: noqa: S605,S607,RUF001
import builtins
import os
from types import CodeType, FrameType
from typing import Any

from rich.console import Console

console = Console(log_time=False, log_path=False)


__builtins__["print"] = console.print


def get_legb(name: str, frame: FrameType | None) -> None:
    # clear_terminal()

    internal_success = info_local
    internal_error = error_local
    legb_letters = ""

    if frame is None:
        internal_error("Frame vazio")
        return

    info_python(f"Vou procurar {name!r} pra você!")

    current = frame
    f_type = ""
    scope_counter = 0
    should_raise = False

    while current:
        f_name = current.f_code.co_name

        if f_name == "<module>":
            f_type = "Global"
            internal_success = success_global
            internal_error = error_global
            legb_letters += "G"
        elif f_type == "":
            f_type = "Local"
            internal_success = success_local
            internal_error = error_local
            legb_letters += "L"
        else:
            f_type = "Enclosing"
            internal_success = success_enclosing
            internal_error = error_enclosing
            legb_letters += "E"

        if name in current.f_locals:
            internal_success(
                f"{name!r} encontrado em {f_name!r}", indent_width=scope_counter
            )
            break
        internal_error(
            f"Nome {name!r} NÃO ENCONTRADO em {f_name!r}", indent_width=scope_counter
        )

        current = current.f_back
        scope_counter += 1

    else:
        f_type = "Built-In"
        f_name = "builtins"
        legb_letters += "B"

        if hasattr(builtins, name):
            success_builtin(
                f" {name!r} encontrado em {f_name!r}", indent_width=scope_counter
            )
        else:
            error_builtin(
                f"Nome {name!r} NÃO ENCONTRADO em {f_name!r}",
                indent_width=scope_counter,
            )
            error(
                f"❌❌❌ NameError: name {name!r} is not defined ",
                indent_width=scope_counter,
            )
            should_raise = True

    print()
    info_kwargs = {
        "style": "dim italic cyan",
        "icon": "👀",
        "line_info": "Info",
        "after": "",
    }
    info(f"Nome pesquisado: {name!r}", **info_kwargs)
    info(f"Escopos não locais pesquisados: {scope_counter}", **info_kwargs)
    info(f"Representação da regra de busca: {legb_letters!r}", **info_kwargs)
    info(f"Exceção de `NameError`: {should_raise}", **info_kwargs)
    print()
    print("-" * 80, end="\n\n")


def get_all_names(code: CodeType) -> None:
    print()
    info(f"Tipos de variáveis em {code.co_name!r}", line_info="Info", sep=" ")
    print()
    info(*code.co_freevars, line_info="Freevars", sep=" ")
    info(*code.co_varnames, line_info="Varnames", sep=" ")
    info(*code.co_cellvars, line_info="Cellvars", sep=" ")
    print()


def clear_terminal() -> None:
    system = os.name  # 'posix', 'nt', 'java'

    if system == "nt":
        os.system("cls")
    elif system == "posix":
        os.system("clear")
    else:
        # fallback
        print("\n" * 100)


def nice_print(
    *values: str,
    icon: str = "",
    line_info: str = "",
    line_info_width: int = 9,
    before: str = "",
    after: str = "",
    sep: str = "",
    end: str = "\n",
    indent: str = "❯",
    indent_width: int = 0,
    style: str = "",
) -> None:
    line_info = f"{line_info: ^{line_info_width}}"
    indent = f" {indent * indent_width} " if indent_width > 0 else " "

    console.print(before, sep="", end="")
    console.print(
        f"[ {icon} {line_info} ]{indent}",
        *values,
        sep=sep,
        end=end,
        style=style,
    )
    console.print(after, sep="", end="")


def success(
    *values: str,
    icon: str = "🟢",
    line_info: str = "Success",
    indent_width: int = 0,
    after: str = "",
    style: str = "color(46)",
) -> None:
    nice_print(
        *values,
        icon=icon,
        line_info=line_info,
        indent_width=indent_width,
        after=after,
        style=style,
    )


def info(
    *values: str,
    icon: str = "🔵",
    line_info: str = "Info",
    indent_width: int = 0,
    after: str = "",
    style: str = "blue",
    **kwargs: dict[str, Any],
) -> None:
    nice_print(
        *values,
        icon=icon,
        line_info=line_info,
        indent_width=indent_width,
        after=after,
        style=style,
        **kwargs,
    )


def error(
    *values: str,
    icon: str = "🔴",
    line_info: str = "Error",
    indent_width: int = 0,
    after: str = "",
    style: str = "red",
) -> None:
    nice_print(
        *values,
        icon=icon,
        line_info=line_info,
        indent_width=indent_width,
        after=after,
        style=style,
    )


def info_python(*values: str) -> None:
    info(*values, icon="🐍", line_info="Python", after="\n", style="blue bold")


def info_local(*values: str, indent_width: int = 0) -> None:
    info(*values, line_info="Local", indent_width=indent_width)


def info_enclosing(*values: str, indent_width: int = 0) -> None:
    info(*values, line_info="Enclosing", indent_width=indent_width)


def info_global(*values: str, indent_width: int = 0) -> None:
    info(*values, line_info="Global", indent_width=indent_width)


def info_builtin(*values: str, indent_width: int = 0) -> None:
    info(*values, line_info="BuiltIn", indent_width=indent_width)


def error_local(*values: str, indent_width: int = 0) -> None:
    error(*values, line_info="Local", indent_width=indent_width)


def error_enclosing(*values: str, indent_width: int = 0) -> None:
    error(*values, line_info="Enclosing", indent_width=indent_width)


def error_global(*values: str, indent_width: int = 0) -> None:
    error(*values, line_info="Global", indent_width=indent_width)


def error_builtin(*values: str, indent_width: int = 0) -> None:
    error(*values, line_info="Built-In", indent_width=indent_width)


def success_local(*values: str, indent_width: int = 0) -> None:
    success(*["🏁", *values], line_info="Local", indent_width=indent_width)


def success_enclosing(*values: str, indent_width: int = 0) -> None:
    success(*["🏁", *values], line_info="Enclosing", indent_width=indent_width)


def success_global(*values: str, indent_width: int = 0) -> None:
    success(*["🏁", *values], line_info="Global", indent_width=indent_width)


def success_builtin(*values: str, indent_width: int = 0) -> None:
    success(*["🏁", *values], line_info="Built-In", indent_width=indent_width)


__builtins__["get_legb"] = get_legb
__builtins__["get_all_names"] = get_all_names

print()
