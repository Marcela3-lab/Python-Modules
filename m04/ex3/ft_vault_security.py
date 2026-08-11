def secure_archive(nome_arquivo: str, acao: str =
                   "read", conteudo: str = "") -> tuple:
    try:
        if acao == "read":
            with open(nome_arquivo, "r") as archive:
                dados = archive.read()
                print("Using 'secure_archive' to read from a regular file:")
                return (True, dados)
        else:
            with open(nome_arquivo, "w") as archive:
                archive.write(conteudo)
                print("Using 'secure_archive' to write previous "
                      "content to a new file:")
                return (True, "Content successfully written to file")
    except FileNotFoundError as e:
        print("Using 'secure_archive' to read from a nonexistent file:")
        return (False, str(e))
    except PermissionError as e:
        print("Using 'secure_archive' to read from an inaccessible file:")
        return (False, str(e))


print("=== Cyber Archives Security ===")
resultado = secure_archive("aa.txt", "write", "aabc")
print(resultado)
