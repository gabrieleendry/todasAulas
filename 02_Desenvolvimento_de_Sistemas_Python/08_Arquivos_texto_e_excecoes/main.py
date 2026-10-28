from subalgs import *
import os

# dados iniciais
arquivo = 'jogos.json'
campos = ['codigo', 'titulo', 'genero', 'ano']
jogos = []
carregar_dados(arquivo, jogos)


# menu principal
while True:
        mostrar_menu()
        opcao = input('Escolha: ').strip()

        match opcao:
            case '0':
                mostrar_aviso('Programa encerrado.')
                break

            case '1':
                codigo = input('Codigo: ').strip()
                while not texto_valido(codigo):
                    mostrar_aviso('O codigo nao pode ficar vazio.')
                    codigo = input('Codigo: ').strip()

                if buscar_indice(jogos, 'codigo', codigo) != -1:
                    mostrar_aviso('Este codigo ja existe.')
                else:
                    titulo = input('Titulo: ').strip()
                    while not texto_valido(titulo):
                        titulo = input('Titulo: ').strip()

                    genero = input('Genero: ').strip()
                    while not texto_valido(genero):
                        genero = input('Genero: ').strip()

                    ano = input('Ano: ').strip()
                    while not ano_valido(ano):
                        mostrar_aviso('Digite um ano entre 1950 e 2026.')
                        ano = input('Ano: ').strip()

                    jogo = criar_registro(codigo, titulo, genero, int(ano))
                    adicionar_registro(jogos, jogo)
                    salvar_dados(arquivo, jogos)

            case '2':
                mostrar_lista(jogos, campos)

            case '3':
                codigo = input('Codigo para buscar: ').strip()
                indice = buscar_indice(jogos, 'codigo', codigo)

                if indice == -1:
                    mostrar_aviso('Jogo nao encontrado.')
                else:
                    mostrar_registro(jogos[indice], campos)

            case '4':
                codigo = input('Codigo para editar: ').strip()
                indice = buscar_indice(jogos, 'codigo', codigo)

                if indice == -1:
                    mostrar_aviso('Jogo nao encontrado.')
                    resposta = input('Deseja cadastrar? (s/n): ').strip().lower()
                    while not opcao_valida(resposta, ['s', 'n']):
                        resposta = input('Digite s ou n: ').strip().lower()

                    if resposta == 's':
                        if not texto_valido(codigo):
                            mostrar_aviso('O codigo nao pode ficar vazio.')
                        else:
                            titulo = input('Titulo: ').strip()
                            while not texto_valido(titulo):
                                titulo = input('Titulo: ').strip()

                            genero = input('Genero: ').strip()
                            while not texto_valido(genero):
                                genero = input('Genero: ').strip()

                            ano = input('Ano: ').strip()
                            while not ano_valido(ano):
                                mostrar_aviso('Digite um ano entre 1950 e 2026.')
                                ano = input('Ano: ').strip()

                            jogo = criar_registro(codigo, titulo, genero, int(ano))
                            adicionar_registro(jogos, jogo)
                            salvar_dados(arquivo, jogos)
                else:
                    mostrar_registro(jogos[indice], campos)
                    mostrar_aviso('Enter mantem o valor atual.')

                    for campo in campos[1:]:
                        atual = obter_valor(jogos[indice], campo)
                        novo = input(campo.capitalize() + ' (' + atual + '): ').strip()

                        if texto_valido(novo):
                            if campo == 'ano':
                                while not ano_valido(novo):
                                    mostrar_aviso('Digite um ano entre 1950 e 2026.')
                                    novo = input('Ano: ').strip()
                                editar_campo(jogos[indice], campo, int(novo))
                            else:
                                editar_campo(jogos[indice], campo, novo)

                    salvar_dados(arquivo, jogos)

            case '5':
                codigo = input('Codigo para excluir: ').strip()
                indice = buscar_indice(jogos, 'codigo', codigo)

                if indice == -1:
                    mostrar_aviso('Jogo nao encontrado.')
                else:
                    mostrar_registro(jogos[indice], campos)
                    resposta = input('Confirma exclusao? (s/n): ').strip().lower()
                    while not opcao_valida(resposta, ['s', 'n']):
                        resposta = input('Digite s ou n: ').strip().lower()

                    if resposta == 's':
                        excluir_registro(jogos, indice)
                        salvar_dados(arquivo, jogos)
                    else:
                        mostrar_aviso('Exclusao cancelada.')

            case _:
                mostrar_aviso('Opcao invalida.')


