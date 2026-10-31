import argparse
import os

# Cores ANSI para interface de linha de comando moderna
RED = "\033[38;5;196m"
GREEN = "\033[38;5;46m"
GOLD = "\033[38;5;220m"
WHITE = "\033[38;5;255m"
GRAY = "\033[38;5;245m"
DIM = "\033[2m"
RESET = "\033[0m"
BOLD = "\033[1m"


def minify_js(source: str) -> str:
    """Minify JavaScript code by removing comments and unnecessary whitespace."""
    out = []
    i = 0
    n = len(source)
    state = "normal"
    delim = ""

    while i < n:
        c = source[i]
        nc = source[i + 1] if i + 1 < n else ""

        if state == "normal":
            if c == "/" and nc == "/":
                i += 2
                while i < n and source[i] not in "\r\n":
                    i += 1
                continue
            if c == "/" and nc == "*":
                i += 2
                while i < n - 1 and not (source[i] == "*" and source[i + 1] == "/"):
                    i += 1
                i += 2
                continue
            if c in ('"', "'"):
                delim = c
                state = "string"
                out.append(c)
                i += 1
                continue
            if c == "`":
                state = "template"
                out.append(c)
                i += 1
                continue
            if c.isspace():
                j = i + 1
                while j < n and source[j].isspace():
                    j += 1
                if out:
                    prev = out[-1]
                    next_char = source[j] if j < n else ""
                    if (
                        prev not in " "
                        and prev not in "([{,;:+-*/%&|^!~=<>?"
                        and next_char not in " \")]}},;:+-*/%&|^!~=<>?"
                        and next_char != ""
                    ):
                        out.append(" ")
                i = j
                continue
            out.append(c)
            i += 1
            continue

        if state == "string":
            out.append(c)
            if c == "\\":
                if i + 1 < n:
                    out.append(source[i + 1])
                    i += 2
                    continue
            if c == delim:
                state = "normal"
            i += 1
            continue

        if state == "template":
            out.append(c)
            if c == "\\":
                if i + 1 < n:
                    out.append(source[i + 1])
                    i += 2
                    continue
            if c == "`":
                state = "normal"
                i += 1
                continue
            if c == "$" and nc == "{":
                out.append(nc)
                i += 2
                continue
            i += 1
            continue

    return "".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=f"{BOLD}{GOLD}Smart Minifier{RESET} {DIM}- Minificador de código JavaScript{RESET}"
    )
    parser.add_argument("source", help="Caminho do arquivo JavaScript de entrada.")
    parser.add_argument("-o", "--output", help="Caminho do arquivo de saída minificado.")
    args = parser.parse_args()

    if not os.path.isfile(args.source):
        raise FileNotFoundError(f"{RED}Arquivo não encontrado:{RESET} {args.source}")

    with open(args.source, "r", encoding="utf-8") as infile:
        source_code = infile.read()

    minified = minify_js(source_code)

    output_path = args.output or f"{os.path.splitext(args.source)[0]}.min.js"
    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write(minified)

    orig_size = len(source_code)
    min_size = len(minified)
    saved = orig_size - min_size
    pct = (saved / orig_size * 100) if orig_size else 0

    print()
    print(f"{BOLD}{WHITE}>> Minificacao concluida{RESET}")
    print(f"{BOLD}{WHITE}  >{RESET} {GRAY}Entrada:{RESET}      {args.source}")
    print(f"{BOLD}{WHITE}  >{RESET} {GRAY}Saida:{RESET}        {output_path}")
    print(f"{BOLD}{WHITE}  >{RESET} {GRAY}Tamanho original:{RESET} {orig_size:,} bytes")
    print(f"{BOLD}{WHITE}  >{RESET} {GRAY}Tamanho minificado:{RESET} {min_size:,} bytes")
    print(f"{BOLD}{WHITE}  >{RESET} {GRAY}Economia:{RESET} {GREEN}{saved:,} bytes ({pct:.1f}%){RESET}")
    print()


if __name__ == "__main__":
    main()
