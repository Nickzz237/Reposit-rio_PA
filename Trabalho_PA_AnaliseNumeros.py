numeros = []
for contador in range(15):
    lista = int(input(f"Digite o {contador+1}º número da lista: "))
    numeros.append(lista)

ordenados = sorted(numeros)
print(f"Essa é sua lista em ordem crescente: {ordenados}")


pares = 0
impares = 0
for n in numeros:
    if n % 2 == 0:
        pares +=1
    else:
        impares +=1

print(f"A lista que você montou tem {pares} números pares, e {impares} números impares.")
input("Pressione Enter para finalizar o programa.")