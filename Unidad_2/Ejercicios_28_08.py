#Ejercicio_1
#La universidad desea automatizar la postulación a becas
#nombre=str(input("Nombre y Apellido: "))
#edad=int(input("Ingrese su edad: "))
#promedio=float(input("Ingrese su promedio general: "))
#ingresos=float(input("Ingresos familiares mensuales: "))

#Ejercicio_2
#Un hospital quiere organizar turnos según el tipo de paciente. El sistema debe pedir:
nombre=str(input("Nombre y Apellido: "))
dni=int(input("Ingrese su DNI: "))

if dni>1000000 and dni<99999999:
    edad=int(input("Ingrese su edad: "))
    obra_social=str(input("Tiene obra social SI/NO ?: ")).lower()
    prioridad=int(input("Cual es su prioridad 1 = emergencia, 2 = urgente, 3 = control?: "))
    if prioridad==1:
        print("Usted fue asignado a la guardia")
    elif prioridad==2:
        if obra_social=="si":
            print("Usted tiene turno en 24 hs")
        else:
            print("Usted tiene turno en 48 hs")
    else:
        if edad>65:
            print("Usted tiene turno en 72 hs")
        else:
            print("Usted tiene turno en 7 dias")
else:
    print("El dni ingresado es invalido")