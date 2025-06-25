#GERADOR DE TABUADA
i = 1
numero = int(input("Por favor, informe o valor do qual deseja a tabuada: "))

while (i <= 10):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i = i + 1
print("-----------------------------------------------------")

#tabuada com for - tipo 1
n = int(input("Informe o valor desejado para obter a tabuada: "))
for contd in range(1, 10, 1):
    print(contd * n)

print("-----------------------------------------------------")
#tabuada com for - tipo 2
nt = int(input("Informe o valor desejado para obter a tabuada: "))
for contt in range(nt, nt * 10 + 1, nt):
    print(contt)

