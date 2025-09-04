
# Patente inicial
l1 = 'A'
l2 = 'A'
l3 = 'A'
n = 0

# Ingresar cantidad a sumar
cantidad = int(input("¿Cuántas patentes querés sumar?: "))

# Sumar patentes usando solo for
for i in range(cantidad):
    n += 1
    if n > 999:
        n = 0
        l3 = chr(ord(l3) + 1)
        if l3 > 'Z':
            l3 = 'A'
            l2 = chr(ord(l2) + 1)
            if l2 > 'Z':
                l2 = 'A'
                l1 = chr(ord(l1) + 1)

# Mostrar resultado
print("Patente final:", l1 + l2 + l3 + f"{n:03d}")
