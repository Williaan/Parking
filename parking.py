# coding: utf-8
from time import sleep

print("->>ESTACIONAMENTO DE VEÍCULOS<<-")
print()
while True:
  op = int(input("ESCOLHA UMA DAS OPÇÕES ABAIXO: \n 1 - Moto \n 2 - Carro \n 3 - Sair \n >: "))
  print(20*"**")
  if op == 1:
    tempo = float(input("Quanto tempo ficou estacionado?\n (OBS: só informar valor inteiro)\n>: "))
    vH = 4
    soma = vH * tempo
    print()
    print(15*"-=")
    print("Você ficou", tempo,"horas,","\nSeu saldo a pagar é de R$:",soma,"reais")
    print(18*"-=")
    print()
    print(20*"**")
  elif op == 2:
    tempo = float(input("Quanto tempo ficou estacionado?:\n (OBS: só informar valor inteiro)\n>: "))
    vH = 7
    soma = vH * tempo
    print()
    print(15*"-=")
    print("Você ficou", tempo,"horas,","\nSeu saldo a pagar é de R$:",soma,"reais")
    print(18*"-=")
    print()
    print(20*"**")
  elif op == 3:
   break
  else:
    print("ERRO: Informe um número válido!")
    print(20*"**")
    print()
print("Saindo..")
sleep(3)
print("OBRIGADO PELA PREFERÊNCIA,VOLTE SEMPRE!!!")
