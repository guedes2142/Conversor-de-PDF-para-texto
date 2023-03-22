# Por: Rafael Guedes
# PDF => Texto
# Linux-Ubunto
# 22/03/2023

from PyPDF2 import PdfReader
from colorama import Fore, Style
import os
os.system('clear')

print(Fore.GREEN + ' ███████████  ██████████   ███████████    ███████████    ███████       ███████████ ██████████ █████ █████ ███████████' + Style.RESET_ALL)
print(Fore.RED + '░░███░░░░░███░░███░░░░███ ░░███░░░░░░█   ░█░░░███░░░█  ███░░░░░███    ░█░░░███░░░█░░███░░░░░█░░███ ░░███ ░█░░░███░░░█' + Style.RESET_ALL)
print(Fore.YELLOW + ' ░███    ░███ ░███   ░░███ ░███   █ ░    ░   ░███  ░  ███     ░░███   ░   ░███  ░  ░███  █ ░  ░░███ ███  ░   ░███  ░ ' + Style.RESET_ALL)
print(Fore.BLUE + ' ░██████████  ░███    ░███ ░███████          ░███    ░███      ░███       ░███     ░██████     ░░█████       ░███    ' + Style.RESET_ALL)
print(Fore.CYAN + ' ░███░░░░░░   ░███    ░███ ░███░░░█          ░███    ░███      ░███       ░███     ░███░░█      ███░███      ░███    ' + Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX + ' ░███         ░███    ███  ░███  ░           ░███    ░░███     ███        ░███     ░███ ░   █  ███ ░░███     ░███    ' + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + ' █████        ██████████   █████             █████    ░░░███████░         █████    ██████████ █████ █████    █████   ' + Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX + '░░░░░        ░░░░░░░░░░   ░░░░░             ░░░░░       ░░░░░░░          ░░░░░    ░░░░░░░░░░ ░░░░░ ░░░░░    ░░░░░    ' + Style.RESET_ALL)
print('by. Rafael Guedes / Github: github.com/guedes2142 ')

while True:
    print()
    # pegando caminho do arquivo 
    
    print(Fore.YELLOW +'O arquivo deve estár na mesma página que este programa!' + Style.RESET_ALL)
    print(Fore.YELLOW + 'Exemplo: nomearquivo.pdf ' + Style.RESET_ALL)
    print('Para sair a qualquer momento digite sair')
    print()
    arquivo = input (Fore.GREEN + 'Nome do arquivo [com .pdf no final]: ' + Style.RESET_ALL)
    print()

    # definindo regras
    if arquivo == 'sair':
        break
    else:
        pass
    if '.pdf' not in arquivo:
        print(Fore.RED +'arquivo inválido' + Style.RESET_ALL)
        continue
    elif arquivo == '':
        print(Fore.RED +'você não selecionou nenhum arquivo!' + Style.RESET_ALL)
        continue
    else:
        pass
    
    # nome de saida do arquivo
    nome_arquivo = input (Fore.GREEN + 'Digite o nome de saida do arquivo : ' + Style.RESET_ALL)

    if nome_arquivo == '':
        print(Fore.RED +'Você não digitou um nome de saida para o novo arquivo' + Style.RESET_ALL)
        continue
    else:
        pass

    #lendo pdf
    reader = PdfReader(arquivo)

    #pegando numero de páginas
    paginas_num = len(reader.pages)

    # armazenando texto
    texto = ''
    # definindo número da página
    num_pagina = 0

    # pegando poginas uma por uma
    for i in range(paginas_num):

        paginaObj =  reader.pages[num_pagina]
        num_pagina += 1
        paginas = paginaObj.extract_text()

        texto += paginas
    try:
        # salvando em arquivo .txt
        with open(f'{nome_arquivo}.txt', 'a+') as file:
            salvar = file.write(texto)
        
        if salvar:
            print('Seu arquivo foi convertido com sucesso')
            continuar = input ('Deseja converter outro arquivo? [S/n] : ').lower()
            if continuar.startswith('s'):
                continue
            else:
                break
        else:
            print(f'Erro ao converter o arquivo,{nome_arquivo}')

    except:
        print('Erro --->>>', e)
        continue





    
   















