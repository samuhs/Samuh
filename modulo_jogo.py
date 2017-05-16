class jogo:

    def __init__(self):

        self.tamanho = 7

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

        pos1 = []
        pos1 = self.escolher_peca()
        if self.matriz[pos1[0]][pos1[1]] != 1:
            return print("\t**Jogada Invalida!**\n")

        letra = []
        verificador,letra = self.verificador_de_movimento(pos1)

        if len(letra) == 0:
            return print("\t**Sem Movimentos possiveis para esta peça!**")

        if verificador and len(pos1) != 0:
            print ("\tPossiveis Movimento: ",letra)
            mov = input("\tPara onde mover a peca: ")

            direcao = self.direcao_mov(letra)
        if mov in direcao:
            self.matriz[pos1[0]][pos1[1]] = ' '
            self.preencher_tabuleiro(mov,pos1)
            self.print_tabuleiro()
        else:
            print ("\n**Movimento Invalido!**\n")

    def verificador_de_movimento(self,pos1):

        verif = False

        letras = []

        down = pos1[0]+2
        if down < 7:
            if self.matriz[down][pos1[1]] == ' ' and self.matriz[pos1[0]+1][pos1[1]] == 1:
                letras.append('Baixo')
                verif = True

        up = pos1[0]-2
        if up >= 0:
            if self.matriz[up][pos1[1]] == ' ' and self.matriz[pos1[0]-1][pos1[1]] == 1:
                letras.append('Cima')
                verif =True

        right = pos1[1]+2
        if right < 7:
            if self.matriz[pos1[0]][right] == ' ' and self.matriz[pos1[0]][pos1[1]+1] == 1:
                letras.append('Direita')
                verif = True

        left = pos1[1]-2
        if left >= 0:
            if self.matriz[pos1[0]][left] == ' ' and self.matriz[pos1[0]][pos1[1]-1] == 1:
                letras.append('Esquerda')
                verif = True

        return(verif,letras)

    def preencher_tabuleiro(self,letra,pos1):

            if letra == 's':
                self.matriz[pos1[0]+1][pos1[1]] = ' '
                self.matriz[pos1[0]+2][pos1[1]] = 1

            elif letra == 'w':
                self.matriz[pos1[0]-1][pos1[1]] = ' '
                self.matriz[pos1[0]-2][pos1[1]] = 1

            elif letra == 'd':
                self.matriz[pos1[0]][pos1[1]+1] = ' '
                self.matriz[pos1[0]][pos1[1]+2] = 1

            elif letra == 'a':
                self.matriz[pos1[0]][pos1[1]-1] = ' '
                self.matriz[pos1[0]][pos1[1]-2] = 1

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
        pos1 = []
        print("\tPeça que deseja mover:")

        x = int(input("\tLinha de onde a peça esta: "))
        if x > 7:
            return print("**Esta peça não existe!**")
        else:
            pos1.append(x-1)

        x = int(input("\tColuna de onde a peça esta: "))
        if x >7:
            return print("**Esta peça não existe!**")
        else:
            pos1.append(x-1)

        return (pos1)

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

teste = jogo()
#pos1 = [1,3]
#teste.fim_do_jogo()
#teste.fim_do_jogo()
#print('\n')
#teste.movimento()
