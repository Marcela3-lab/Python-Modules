import sys
import typing


def read_archive(nome_arquivo: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
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

        linhas = conteudo.split("\n")
        linhas_char = [linha + "#" for linha in linhas]
        novo_conteudo = "\n".join(linhas_char)
        print(" ")
        print("Transform data:")
        print("---\n\n")
        print(novo_conteudo)

        print("---\n\n")
        novo_name = input("Enter new file name (or empty): ")

        if novo_name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{novo_name}'")
            novo_arquivo = open(novo_name, "w")
            novo_arquivo.write(novo_conteudo)
            novo_arquivo.close()
            print(f"Data saved in file '{novo_name}'")


args = sys.argv[1:]
if len(args) != 1:
    print("Usage: ft_ancient_text.py <file>")
else:
    read_archive(args[0])
