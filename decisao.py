#!/usr/bin/python3

# Decisões Aninhadas

## Cálculo do IMC
### Fórmula : peso (kg) / (altura ** 2)
### Intervalos:
#### Baico peso: < 18.5
#### Peso normal: 18.5.0 < peso < 24.9
#### Pré obesidade: 25.0 < 29.9
#### Obsidade grau I: 30.0 < 34.9
#### Obesidade grau II: 35.0 - 39.9
#### Obesidade grau III: > 40.


#1: Capturar as informaçãoes de peso e altura
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

#2: Calcular o índice do IMC
imc = peso / (altura ** 2)

#3: Classificar o IMC
if imc < 18.5:
    print(f'Baixo peso - IMC: {imc:.2f}')
elif imc < 24.9:
    print(f'Peso normal - IMC: {imc:.2f}')
elif imc < 29.9:
    print(f'Pré obesidade - IMC: {imc:.2f}')
elif imc < 34.9:  
    print(f'Obsedade Grau I - IMC: {imc:.2f}')
elif imc < 39.9:
    print(f'Obesidade Grau II - IMC: {imc:.2f}')
else:
    print(f'Obesidade Grau III - IMC: {imc:.2f}')

