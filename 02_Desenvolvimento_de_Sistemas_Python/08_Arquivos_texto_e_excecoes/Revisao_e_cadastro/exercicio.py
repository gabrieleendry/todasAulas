import os
os.system("cls")

while True:
    print("""
 0 - Sair         
 1 - Cadastrar Funcionário          
 2 - Exibir Arquivo
 3 - Pesquisar
 
 Escolha: """)
    opcao = int(input("Escolha uma opção: "))
    match opcao:
      case 0:
          break
      case 1:
        nomeU = str(input("Digite seu nome: "))
        idadeU = int(input("Digite sua idade: "))
        alturaU = float(input("Digite sua altura: "))

        dados = "Cadastro" + ".txt"
        arq = open(dados, "a", encoding="utf-8")
        arq.write(f"{nomeU},{idadeU},{alturaU}\n")
        arq.close()
      case 2:
          with open("Cadastro.txt", "r", encoding="utf-8") as dados:
             print(dados.read())
      case 3:
        escolha31 = int(input("1 - Nome\n2 - Idade\n3 - Altura"))
        match escolha31:
            case 1: 
                nome_lista = str(input("Digite o nome que quer encontrar: "))
                with open("Cadastro.txt", "r", encoding="utf-8") as dados:
                    for lista in dados:
                        lista = lista.split(",")
                    if lista[0] == nome_lista:
                        print(f"Nome = {lista[0]}")
                        print(f"Idade = {lista[1]}")
                        print(f"Altura = {lista[2]}")
                        continue
                    else:
                        print("Não existe!")
                    break
                        
            case 2:     
                escolha3 = int(input("1 - Simples\n2 - Maior ou igual\n3 - Menor ou igual\n4 - Entre"))
                match escolha3:
                    case 1:
                        idade_lista = str(input("Digite a idade que quer encontrar: "))
                        with open("Cadastro.txt", "r", encoding="utf-8") as dados:
                            for lista in dados:
                                lista = lista.split(",")
                                if lista[0] == idade_lista:
                                    print(f"Nome = {lista[0]}")
                                    print(f"Idade = {lista[1]}")
                                    print(f"Altura = {lista[2]}")
                                    continue
                                else:
                                    print("Não existe!")
                                    break
                    case 2:
                        idade_lista = str(input("Digite a idade que quer encontrar: "))
                        with open("Cadastro.txt", "r", encoding="utf-8") as dados:
                            for lista in dados:
                                lista = lista.split(",")
                                if lista[0] >= idade_lista:
                                    print(f"Nome = {lista[0]}")
                                    print(f"Idade = {lista[1]}")
                                    print(f"Altura = {lista[2]}")
                                    continue
                                else:
                                    print("Não existe!")
                                    break
                    case 3:
                        idade_lista = str(input("Digite a idade que quer encontrar: "))
                        with open("Cadastro.txt", "r", encoding="utf-8") as dados:
                            for lista in dados:
                                lista = lista.split(",")
                                if lista[0] <= idade_lista:
                                    print(f"Nome = {lista[0]}")
                                    print(f"Idade = {lista[1]}")
                                    print(f"Altura = {lista[2]}")
                                    continue
                                else:
                                    print("Não existe!")
                                    break           
            case 3:
                escolha3 = int(input("1 - Simples\n2 - Maior ou igual\n3 - Menor ou igual\n4 - Entre"))
                match escolha3:
                    case 1:
                        idade_lista = str(input("Digite a Altura que quer encontrar: "))
                        with open("Cadastro.txt", "r", encoding="utf-8") as dados:
                            for lista in dados:
                                lista = lista.split(",")
                                if lista[0] == idade_lista:
                                    print(f"Nome = {lista[0]}")
                                    print(f"Idade = {lista[1]}")
                                    print(f"Altura = {lista[2]}")
                                    continue
                                else:
                                    print("Não existe!")
                                    break
                    case 2:
                        idade_lista = str(input("Digite a Altura que quer encontrar: "))
                        with open("Cadastro.txt", "r", encoding="utf-8") as dados:
                            for lista in dados:
                                lista = lista.split(",")
                                if lista[0] >= idade_lista:
                                    print(f"Nome = {lista[0]}")
                                    print(f"Idade = {lista[1]}")
                                    print(f"Altura = {lista[2]}")
                                    continue
                                else:
                                    print("Não existe!")
                                    break
                    case 3:
                        idade_lista = str(input("Digite a Altura que quer encontrar: "))
                        with open("Cadastro.txt", "r", encoding="utf-8") as dados:
                            for lista in dados:
                                lista = lista.split(",")
                                if lista[0] <= idade_lista:
                                    print(f"Nome = {lista[0]}")
                                    print(f"Idade = {lista[1]}")
                                    print(f"Altura = {lista[2]}")
                                    continue
                                else:
                                    print("Não existe!")
                                    break           

'''
              case 3:
          nome_lista = str(input("Digite o nome que quer encontrar: "))
          with open("Cadastro.txt", "r", encoding="utf-8") as dados:
            for lista in dados:
               lista = lista.split(",")
               if lista[0] == nome_lista:
                 print(f"Nome = {lista[0]}")
                 print(f"Idade = {lista[1]}")
                 print(f"Altura = {lista[2]}")
                 continue
            else:
               print("Não existe!")
               break
                  
        


'''
