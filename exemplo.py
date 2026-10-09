produto = "Mouse Gamer WIFI"
valores = [20,71,100,30]
alunos = ["Ana", "Hugo", "Mariana", "Pedro", "Ana Paula",]

item = input("Qual item deseja encontrar? ")

if item.lower() in produto.lower():
    print("Produto encontrado!")
else:
    print("Produto não encontrado.")

def dobrar(valor):
    resultado = valor*2
    return resultado

valores_novos = []

for item in valores:
    valores_novos.append(dobrar(item))

print(valores_novos)
print(valores)

aluno_procurado = input("Digite um nome para procurar: ")
alunos_encontrados = []

for item in alunos.lower():
    alunos_encontrados.append(item)
print(alunos_encontrados)
