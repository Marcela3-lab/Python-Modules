import sys
import typing


def read_archive(nome_arquivo: str) -> None:

    print(f"Accessing file '{nome_arquivo}'")
    try:
        arquivo: typing.IO[str] = open(nome_arquivo)
    except FileNotFoundError as e:
        print(f"Error opening file '{nome_arquivo}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{nome_arquivo}': {e}")
    else:
        conteudo = arquivo.read()
        print("---\n")
        print(conteudo)
        print("\n\n---")
        arquivo.close()
        print(f"File '{nome_arquivo}' closed.")


args = sys.argv[1:]
if len(args) != 1:
    print("Usage: ft_ancient_text.py <file>")
else:
    print("=== Cyber Archives Recovery ===")
    read_archive(args[0])
