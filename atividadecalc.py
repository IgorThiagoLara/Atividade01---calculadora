'''4) Implemente uma calculadora simples em que o usuário digite 2 números e escolhe a operação

5) Usuário digita 2 números

6) Usuário escolhe a opção (1 - soma ; 2 -  subtração ; 3 - multiplicação ; 4 - divisão ; 5 - sair )

7) Imprima a operação que foi feita e o resulado. Por exemplo: "A operação foi soma: 5+7 = 12")'''

print("Digite dois números!")
num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))

print('''
[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão
[5] Sair''')

cont = 0
while cont == 0:
    escolha = int(input("Agora escolha qual operação deseja que seja efetuada: "))

    if escolha <=0 or escolha >=6:
        print("Número digitado inválido, tente novamente!")
        continue
    cont = cont + 1

    if escolha ==1:
        resultado1 = num1+num2
        print(F"A operação escolhida foi soma: {num1}+{num2} = {resultado1}")

    elif escolha ==2:
        resultado2 = num1-num2
        print(f"A operação escolhida foi a subtração: {num1}-{num2} = {resultado2}")

    elif escolha ==3:
        resultado3 = num1*num2
        print(f"A operação escolhida foi a multiplicação: {num1}*{num2} = {resultado3}")

    elif escolha ==4:
        resultado4 = num1/num2
        print(f"A operação escolhida foi a divisão: {num1}/{num2} = {resultado4}")
        
    elif escolha ==5:
        print("Saindo...")
print("Acabou")