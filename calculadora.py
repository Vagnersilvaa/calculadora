def calculadora(variavel1, variavel2,  operacao):
    if operacao == '+':
        resultado = variavel1 + variavel2 
    elif operacao == '-':
        resultado = variavel1 - variavel2 
    elif operacao == '*':
        if variavel2 != 0 :
            resultado = variavel1 / variavel2 
        else:
            resultado = "Não é possível dividir por zero."
    else:
        resultado = "Operação inválida."

    return resultado

# Exemplo de uso
var1 = float(input("Digite o valor da variável 1: "))
var2 = float(input("Digite o valor da variável 2: "))
op = input("Digite a operação desejada (+, -, *, ): ")

resultado_final = calculadora(var1, var2,  op)
print("Resultado: ", resultado_final)

