#Projeto Educação Infantil - App para controle financeiro

#digite quantas transações você realizou
qtd_trasancoes = int(input("Informe quantas transações você realizou hoje:"))
total_transacoes = 0
#qual o tipo da transação

#quais são os valores da trasanções
for n_transacao in range (1, qtd_trasancoes + 1, 1):
    transacao = float(input("Por favor informe o valor da trasanção nº{}: ".format(n_transacao)))
    total_transacoes = total_transacoes + transacao

media = total_transacoes / qtd_trasancoes

#ficha final
print("Neste dia foi gasto um total de R${}, com uma média de R${} por transação".format(total_transacoes,media))
