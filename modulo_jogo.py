import os
from Solução import *
class jogo:


    def __init__(self):

        self.tamanho = 7
        self.clear = lambda: os.system('cls')

        self.tabuleiro = [ [0, 0, 1, 1, 1, 0, 0],
                           [0, 0, 1, 1, 1, 0, 0],
                           [1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, ' ', 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1],
                           [0, 0, 1, 1, 1, 0, 0],
                           [0 ,0 ,1 ,1 ,1 ,0 ,0] ]

        self.matriz = self.tabuleiro


    def print_tabuleiro(self):

        if self.matriz != self.tabuleiro:
            print('\n')
            for i in range(7):
                linha = self.matriz[i]
                for j in range(7):
                    print(linha[j],end = ' ')
                print('\t',i+1)
            print("\n")
            for i in range(7):
                print(i+1,end = ' ')
            print('\n Cima: w\t Baixo: s\t Direita: d\t Esquerda: a\n')
        else:
            print('\n')
            for i in range(7):
                linha = self.tabuleiro[i]
                for j in range(7):
                    print(linha[j],end = ' ')
                print('\t',i+1)
            print("\n")
            for i in range(7):
                print(i+1,end = ' ')
            print('\n Cima: w\t Baixo: s\t Direita: d\t Esquerda: a\n')


    def movimento(self):

        posicao = []
        posicao = self.escolher_peca()
        if posicao == []:
            return 0
        if self.matriz[posicao[0]][posicao[1]] != 1:
            return print("\t**Jogada Invalida!**\n")

        letra = []
        verificador,letra = self.verificador_de_movimento(posicao)

        if len(letra) == 0:
            return print("\t**Sem Movimentos possiveis para esta peça!**")

        if verificador and len(posicao) != 0:
            print ("\tPossiveis Movimento: ",letra)
            mov = input("\tPara onde mover a peca: ")

            direcao = self.direcao_mov(letra)
        if mov in direcao:
            self.matriz[posicao[0]][posicao[1]] = ' '
            self.preencher_tabuleiro(mov,posicao)
            self.clear()#limpa do prompt

            self.print_tabuleiro()
        else:
            print ("\n**Movimento Invalido!**\n")

    def verificador_de_movimento(self,posicao):

        verif = False

        letras = []

        down = posicao[0]+2
        if down < 7:
            if self.matriz[down][posicao[1]] == ' ' and self.matriz[posicao[0]+1][posicao[1]] == 1:
                letras.append('Baixo')
                verif = True

        up = posicao[0]-2
        if up >= 0:
            if self.matriz[up][posicao[1]] == ' ' and self.matriz[posicao[0]-1][posicao[1]] == 1:
                letras.append('Cima')
                verif =True

        right = posicao[1]+2
        if right < 7:
            if self.matriz[posicao[0]][right] == ' ' and self.matriz[posicao[0]][posicao[1]+1] == 1:
                letras.append('Direita')
                verif = True

        left = posicao[1]-2
        if left >= 0:
            if self.matriz[posicao[0]][left] == ' ' and self.matriz[posicao[0]][posicao[1]-1] == 1:
                letras.append('Esquerda')
                verif = True

        return(verif,letras)

    def preencher_tabuleiro(self,letra,posicao):

            if letra == 's':
                self.matriz[posicao[0]+1][posicao[1]] = ' '
                self.matriz[posicao[0]+2][posicao[1]] = 1

            elif letra == 'w':
                self.matriz[posicao[0]-1][posicao[1]] = ' '
                self.matriz[posicao[0]-2][posicao[1]] = 1

            elif letra == 'd':
                self.matriz[posicao[0]][posicao[1]+1] = ' '
                self.matriz[posicao[0]][posicao[1]+2] = 1

            elif letra == 'a':
                self.matriz[posicao[0]][posicao[1]-1] = ' '
                self.matriz[posicao[0]][posicao[1]-2] = 1

            else:
                print("**Movimento Invalido!**")

    def fim_do_jogo(self):
        count = 0
        for i in range(7):
            linha = self.matriz[i]
            for j in range(7):
                if linha[j] == 1:
                    count=count + 1
        print(count)

    def escolher_peca(self):
        posicao = []
        print("\tPeça que deseja mover:")

        x = int(input("\tLinha de onde a peça esta: "))
        if x == 123:
            print('\n\t**Resolvendo Tabuleiro**')
            solver = Solucao(self.matriz)
            solver.resolver()
            return posicao
        elif x > 7:
            return print("**Esta peça não existe!**")
        else:
            posicao.append(x-1)

        x = int(input("\tColuna de onde a peça esta: "))
        if x >7:
            return print("**Esta peça não existe!**")
        else:
            posicao.append(x-1)

        return (posicao)

    def direcao_mov(self, letra):

        direcao = []

        if 'Direita' in letra:
            direcao.append('d')

        if 'Esquerda' in letra:
            direcao.append('a')

        if 'Cima' in letra:
            direcao.append('w')

        if 'Baixo' in letra:
            direcao.append('s')

        return direcao

    def tem_peca_para_mexer(self):
        for i in range(7):
            for j in range(7):
                if self.movimento_fim(i,j):
                    return True
        return False

    def movimento_fim(self,Linha,Coluna):

        if self.matriz[Linha][Coluna] == 0 or self.matriz[Linha][Coluna]== ' ':
            return False

        down = Linha+2
        if down < 7:
            if self.matriz[down][Coluna] == ' ' and self.matriz[Linha+1][Coluna] == 1:
                return True

        up = Linha-2
        if up >= 0:
            if self.matriz[up][Coluna] == ' ' and self.matriz[Linha-1][Coluna] == 1:
                return True

        right = Coluna+2
        if right < 7:
            if self.matriz[Linha][right] == ' ' and self.matriz[Linha][Coluna+1] == 1:
                return True

        left = Coluna-2
        if left >= 0:
            if self.matriz[Linha][left] == ' ' and self.matriz[Linha][Coluna-1] == 1:
                return True
