from modulo_jogo import jogo

jogar =[]
x=jogo()
jogar.append(x)
i=0

print ("** Resta Um **\n**Tabuleiro **\n")
jogar[i].print_tabuleiro()
print("""\n\t**Para jogar primeiro selecione a peça que deseja mover inserindo
linha e colona da peça respectivamente, depois selecione a direção que deseja mover a peça!*""")
print("\nCaso deseje que a maquina resolva digite 123 em ** Linha de onde a peça esta: ** ")
print("\nDeseja começar a jogar?")
play = input("Tecle S para começar...  ")

while play == 's':
    jogar[i].print_tabuleiro()
    print ('\n')
    while jogar[i].fim_do_jogo != 1:

        solver = jogar[i].movimento()
        if solver == 0:
            print("Jogo resolvido!!\n")
            x=jogo()
            j=jogar.append(x)
            i+=1
            break
        elif jogar[i].fim_do_jogo == 1:
            print("Parabens! Voce Venceu\n")
            x=jogo()
            j=jogar.append(x)
            i+=1
            break

        elif not jogar[i].tem_peca_para_mexer():
            print('** Voce perdeu! =/ **\n')
            x=jogo()
            j=jogar.append(x)
            i+=1
            break

    print(" \nDeseja jogar novamente?")
    play = input("Tecle S para jogar novamente ou N para sair... ")
