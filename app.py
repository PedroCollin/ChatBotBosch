import os
def processar_resposta(resposta,nome):
    if resposta == 1:
        print(f'{os.linesep}{nome}, A bosch é uma empresa onde o seu foco deve ser corta a maior quantia de gastos possivel.{os.linesep}')
    elif resposta == 2:
        print(f'{os.linesep}{nome}, Tenha uma boa relação, porque a empresa é uma grande e maravilhosa empresa!{os.linesep}')
    elif resposta == 3:
        print(f'{os.linesep}{nome}, É um ambiente competitivo e de melhoria constante. O objetivo é melhorar continuamente. A qualidade é a principal preocupação da empresa.{os.linesep}')
    elif resposta == 4:
        print(f'{os.linesep}{nome}, Através do site da empresa - https://www.bosch.com.br/carreiras/ {os.linesep}')
    elif resposta == 5:
        print(f'{os.linesep}{nome}, a bosch conta com Refeição, convênio médico, uniodonto, fretado, área de lazer, desconto na compra de produtos Bosch, plr, desconto farmacia e seguro vida.{os.linesep}')
    elif resposta == 6:
        print(f'{os.linesep}{nome}, Sim, é possível.{os.linesep}')
    elif resposta == 0:
        print(f'{os.linesep}Saindo...{os.linesep}')
        os.system('break')
    else:
        print("Digite algo valido!")

def start():
    # Apresentar o chatbot
    print("Olá, Seja bem vindo ao bot Pedro!")
    # Pedir nome
    nome = input("Digite o seu nome: ")
    # pedir email
    email = input("Digite o seu email: ")

    while True:
    # oferecer o menu de opcoes
        resposta = int(input(f'O que gostaria de saber?{os.linesep}[1] - Se você estivesse no controle, o que você faria para melhorar a empresa Bosch?{os.linesep}[2] - Quais dicas e conselhos você daria para alguém que esteja no processo seletivo na empresa Bosch?{os.linesep}[3] - Como é o ambiente e a cultura da empresa Bosch?{os.linesep}[4] - Como faço para me inscrever para trabalhar na empresa: Bosch?{os.linesep}[5] - Quais os benefícios que a empresa oferece?{os.linesep}[6] - Posso me candidatar para trabalhar em outro país?{os.linesep}[0] - Sair{os.linesep}'))
    # processar respostas
        processar_resposta(resposta,nome)
        os.system('pause')
        os.system('cls')
        if resposta == 0:
            break
if __name__ == '__main__':
    start()