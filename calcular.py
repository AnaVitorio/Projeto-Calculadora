def calculadora():
    numero_escolhido = int(input('Qual é o número que você deseja saber a tabuada?'))
    tabuada = 0
    while tabuada <= 10:
        resultado = numero_escolhido*tabuada
        print(numero_escolhido, 'X', tabuada, '=', resultado)
        tabuada = tabuada + 1
    pergunta = int(input('Você deseja ver a tabuada de outro número? (1-sim/2-não)'))
    if pergunta == 1:
        calculadora()
    elif pergunta == 2:
        print("TCHAU!")
calculadora()
