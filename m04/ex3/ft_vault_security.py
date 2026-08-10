def secure_archive(nome_arquivo: str, acao: str = "read", conteudo: str = "") -> tuple:
    try:
        if acao == "read":
            with open (nome_arquivo, "r") as archive:
                dados = archive.read()
                return (True, dados)
        else: 
            with open (nome_arquivo, "w") as archive:
                archive.write(conteudo)
                return (True, "Content successfully written to file")
    except FileNotFoundError as e:
        return (False, str(e))
    except PermissionError as e:
        return (False, str(e))

print("=== Cyber Archives Security ===")
resultado = secure_archive("aa.txt","write","aabc")
print(resultado)