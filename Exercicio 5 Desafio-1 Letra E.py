menu=""
while(menu !='exit'): 
  print("Escolha o Calculo que Deseja Realizar Abaixo!")
  print("A - Para Soma")
  print("B - Para Subtração")
  print("C - Para Multiplicação")
  print("D - Para Divisão")
  print("Se quiser Sair Digite exit")
  menu = input()
  if menu == 'a':
    a = float(input("Digite um Número Real se você souber :"))
    b = float(input("Digite outro Número Real que eu já sei que você sabe :"))
    soma = a+b
    print("Está é a Soma dos Números Reais:",soma)
  if menu == 'b':
    a = float(input("Digite um Número Real se você souber :"))
    b = float(input("Digite outro Número Real que eu já sei que você sabe :"))
    sub = a-b
    print("Está é a Subtração dos Números Reais:",sub)
  if menu == 'c':
    a = float(input("Digite um Número Real se você souber :"))
    b = float(input("Digite outro Número Real que eu já sei que você sabe :"))
    mult = a*b
    print("Está é a Multiplicação dos Números Reais:",mult)
  if menu == 'd':
    a = float(input("Digite um Número Real se você souber :"))
    b = float(input("Digite outro Número Real que eu já sei que você sabe :"))
    div = a/b
    print("Está é a Divisão dos Números Reais:",div)
  elif menu =='exit':
    print("Programa Encerrado!")