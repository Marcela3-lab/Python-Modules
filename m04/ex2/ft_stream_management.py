import sys
import typing

def read_archive(nome_arquivo: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{nome_arquivo}'")

    try:
        arquivo = open(nome_arquivo)
    except FileNotFoundError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{nome_arquivo}': {e}\n")
    except PermissionError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{nome_arquivo}': {e}\n")
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
        print(novo_conteudo)

        print("---\n\n")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        novo_name = sys.stdin.readline().strip()
        if novo_name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{novo_name}'")
            try:
                novo_arquivo = open(novo_name, "w")
            except PermissionError as e:
                sys.stderr.write(f"[STDERR] Error opening file '{novo_name}' : {e}\n")
                print("Data not saved.")
            except FileNotFoundError as e:
                sys.stderr.write(f"[STDEER] Error opening file '{novo_name}': {e}\n")
                print("Data not saved")
            else:
                novo_arquivo.write(novo_conteudo)
                novo_arquivo.close()
                print(f"Data saved in file '{novo_name}'")


args = sys.argv[1:]
if len(args) != 1:
    print("Usage: ft_ancient_text.py <file>")
else:
    read_archive(args[0])