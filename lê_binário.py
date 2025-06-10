'''def lê_binário():
    try:
        arquivo = open("arquivo.txt" ,"w") 
        arquivo.write("Uma mensagem")
        arquivo.close()
    except FileNotFoundError as e:
        print('Arquivo não existe! -_-|||', e)
    except IOError as e:
        print('Deu algo errado @_@') 
    print("OK! ~_~")
lê_binário()
'''
def lê_binário():
    try:
        with open("números.txt" ,"r") as fs1:
            dados=fs1.read()
            print(type(dados))
        with open("cópia.txt" ,"w") as fs2:
            fs2.write(dados)
        with open("nome.txt" ,"w") as fs2:
            fs2.write(dados)
        with open("último.txt" ,"w") as fs2:
            fs2.write(dados)
    except FileNotFoundError as e:
        print('Arquivo não existe! -_-|||', e)
    except IOError as e:
        print('Deu algo errado @_@') 
    print("OK! ~_~")
lê_binário()
