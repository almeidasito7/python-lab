print("IF ENCADEADO EM PYTHON")
print("----------------------")
print("")

RM = int(input("Por favor, digite seu RM: "))
print("")
I = int(input("Por favor, digite sua idade: "))
print("")

if (I >= 18):
    print(f"Sua participação foi autorizada, alundo de RM {RM}")
    print("Mais informações serão enviadas para o e-mail cadastrado.")
    print("")
else:
    A = (input("Você possui autorização dos seus responsáveis? [S-SIM / N-NÃO]"))
    if (A == 'S'):
        print("Sua participação foi autorizada, Aluno de RM {}!".format(RM))
        print("Mais informações serão enviadas para o e-mail cadastrado.")
        print("")
    else:
        print("Infelizmente sua participação não foi autorizada pela sua idade.")
        print("")
