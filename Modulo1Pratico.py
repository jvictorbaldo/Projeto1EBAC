## Variaveis essenciais para o funcionamento do Código
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
tipo_op = input('Selecionar uma operação ou criar um loop que permita realizar várias operações? \n("O" para Selecionar Operação ou "L" para gerar o Loop): ')
val = numero1


##Calculadora com o usuário selecionando a operação
if tipo_op == 'O':
    operacao = input('Qual o tipo de operação que deseja ultilziar (+, -, *, /): ')

    if operacao == '+':
        print('O resultado é ',numero1 + numero2)
   
    elif operacao == '-':
        print('O resultado é ',numero1 - numero2)
   
    elif operacao == '*':
        print('O resultado é ',numero1 * numero2)
   
    elif operacao == '/':
         if numero2 == 0: ## if/else caso o segundo número tenha sido 0
            print('Erro!\nDivisão por Zero.')
         else:
            print('O resutado é ',numero1 / numero2)

    else:
        print('O resultado é inválido!\nEscolha entre os operadores disponíveis (+, -, *, /). ')


##Calculadora com o usuário selecionando o Loop de Operação

else:    
    if tipo_op == 'L':
        operacao2 = input('Qual a operação que deseja deixar em Loop? (+, -, *, /): ')
       
        if operacao2 == '+':
            while (val < 999999):
                val += numero2
                print(val)
        
        elif operacao2 == '-':
            while (val >= 0):
                val -= numero2
                if val <= 0: ## Temos um if caso o número seja menor que "0" o loop termina
                    break
                print(val)
        
        elif operacao2 == '*':
            while (val <= 999999):
                val *= numero2
                print(val)
        
        elif operacao2 == '/':
            if numero2 == 0:  # Verifica se o segundo número é zero
                print('Erro!\nDivisão por Zero.')
            else:
                while (val > 0):
                    val /= numero2
                    print(val)
                    if val < 1:  # Para o loop se val for menor que 1
                        break


