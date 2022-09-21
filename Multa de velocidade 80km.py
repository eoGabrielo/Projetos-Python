velocidade= int(input("Qual velocidade do veiculo? "))

multa= float(velocidade-80) * 5

if velocidade <= 80:
    print(f"VELOCIDADE PERMITIDA: {velocidade}Km/hora;")
    print("Boa viagem, dirija com segurança.")
else:
    print(f"VELOCIDADE ULTRAPASSADA: {velocidade}Km/hora!!! Velocidade permitida: 80km/hora; ")
    print(f"Sua multa sera de R$5.00 por Km ultrapassado;")
    print(f"Voce foi multado no valor de: R${multa} reais;")
    print("Boa viagem, dirija com segurança.")

#Variavel velocidade recebe a velocidade do veiculo

#Variavel multa calcula a multa, 5 reais p/km ultrapassado.
#pega o valor de velocidade - 80km/h(velocidade permitida) x 5 reais
#da multa por km

#if e else pra se a velocidade for maior ou menor mostra uma mensagem