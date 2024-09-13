
import random
import time


dibujo_dados = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dados= []
total = 0
numero_dados = int(input("¿Cuantos Dados quieres?: "))

for dado in range(numero_dados):
    dados.append(random.randint(1, 6))


#Mostrar Dados en pantalla

print()

print("Tirando los dados")
for x in range(3,0,-1):
    segundos = x%60
    print(f"{segundos:02}")
    time.sleep(1)
print()    
print("Estos son los dados que te salieron")

for linea in range(5):
    for dado in dados:
        print(dibujo_dados.get(dado)[linea], end="")
    print()

for dado in dados:
    total += dado
print(f"La suma da un total de : {total}")