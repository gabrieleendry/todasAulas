import json
import os


# conferir texto
def texto_valido(texto: str) -> bool:
    return texto.strip() != ''


# conferir ano
def ano_valido(texto: str) -> bool:
    return texto.isdigit() and 1950 <= int(texto) <= 2026


# conferir opcao
def opcao_valida(opcao: str, opcoes: list) -> bool:
    return opcao.lower() in opcoes


# conferir igualdade
def valores_iguais(valor1: str, valor2: str) -> bool:
    return str(valor1).lower() == str(valor2).lower()


# achar posicao
def buscar_indice(dados: list, campo: str, valor: str) -> int:
    for i in range(len(dados)):
        if valores_iguais(dados[i].get(campo, ''), valor):
            return i
    return -1


# criar jogo
def criar_registro(codigo: str, titulo: str, genero: str, ano: int) -> dict:
    return {'codigo': codigo, 'titulo': titulo, 'genero': genero, 'ano': ano}


# obter valor
def obter_valor(registro: dict, campo: str) -> str:
    return str(registro.get(campo, ''))


# contar jogos
def contar_registros(dados: list) -> int:
    return len(dados)


# ler arquivo
def carregar_dados(arquivo: str, dados: list):
    if os.path.exists(arquivo):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                conteudo = json.load(f)
            if isinstance(conteudo, list):
                dados.extend(conteudo)
            else:
                print('Arquivo com formato invalido.')
        except (json.JSONDecodeError):
            #parte chata que ficava dando erro por causa das aspas
            print('Nao foi possivel ler os dados.')


# gravar arquivo
def salvar_dados(arquivo: str, dados: list):
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print('Dados salvos!')
    except (TypeError):
        print('Nao foi possivel salvar os dados.')


# adicionar jogo
def adicionar_registro(dados: list, registro: dict):
    dados.append(registro)


# mudar campo
def editar_campo(registro: dict, campo: str, valor: str | int):
    registro[campo] = valor


# remover jogo
def excluir_registro(dados: list, indice: int):
    del dados[indice]


# mostrar aviso
def mostrar_aviso(mensagem: str):
    print(mensagem)


# mostrar jogo
def mostrar_registro(registro: dict, campos: list):
    for campo in campos:
        print(campo.capitalize() + ':', obter_valor(registro, campo))


# mostrar jogos
def mostrar_lista(dados: list, campos: list):
    if contar_registros(dados) == 0:
        mostrar_aviso('Nenhum jogo cadastrado.')
    else:
        for i in range(contar_registros(dados)):
            print('\nJogo', i + 1)
            mostrar_registro(dados[i], campos)


# mostrar menu
def mostrar_menu():
    print('\n--- CADASTRO DE JOGOS ---')
    print('0 - Sair')
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Buscar')
    print('4 - Editar')
    print('5 - Excluir')
