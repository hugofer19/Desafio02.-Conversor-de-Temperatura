print("Deseja inserir a temperatura em graus Celsius ou em Fahrenheit")
print("Celsius = 1")
print("Fahrenheit = 2")
operacao = int(input("Resposta: "))

if operacao == 1:
    cel_recebe = int(input("Coloca os graus Celsius para converter em Fahrenheit: "))
    fah = (cel_recebe * 1.8) + 32
    print("A temperatura de", cel_recebe, "graus Celsius em Fahrenheit é de", fah)
elif operacao == 2:
    fah_recebe = float(input("Coloca os graus Fahrenheit para converter em Celsius: "))
    cel = (fah_recebe - 32) * 5 / 9
    print("A temperatura de", fah_recebe, "graus Fahrenheit em Celsius é de", cel)
else:
    print("Opção invalidida, escolhe apenas a opção 1 ou 2")
