# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7

nota = float(input("  nota 01 : "))
nota2 = float(input("  nota 02 : "))
nota3 = float(input("  nota 03 : "))

def calcular_media(notas):
    media = sum(notas) / len(notas)
    
    if media >= 6.0:
        return media, "Aprovado"
    else:
        return media, "Reprovado"

notas_aluno = [nota, nota2, nota3] 
media, status = calcular_media(notas_aluno)

print(f"Média: {media:.2f}, Status: {status}")