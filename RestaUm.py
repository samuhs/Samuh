from modulo_jogo import jogo


jogar = jogo()

print ("** Resta Um **\n**Tabuleiro **\n")
jogar.print_tabuleiro()
print("""\n\t**Para jogar primeiro selecione a peça que deseja mover inserindo
linha e colona da peça respectivamente, depois selecione a direção que deseja mover a peça!*""")

print("\nDeseja começar a jogar?")
play = input("Tecle S para começar...  ")

while play == 's':
    jogar.print_tabuleiro()
    print ('\n')
    while jogar.fim_do_jogo != 1:


        jogar.movimento()

    if jogar.fim_do_jogo == 1:
        print("Parabens! Voce Venceu")

    print(" \nDeseja jogar novamente?")
    play = input("Tecle S para jogar novamente ou N para sair... ")
