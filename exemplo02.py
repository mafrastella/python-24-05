# calcular média de duas notas e determinar se o aluno está aprovado ou reprovado (media>= 7)

nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))

media = (nota1 + nota2) / 2

print("A media é: " + str(media))

# verifica se aluno foi APROVADO ou REPROVADO
if(media >= 7):
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")