#Ejercicio_1
#La universidad desea automatizar la postulación a becas
nombre_uni=str(input("Nombre y Apellido: "))
edad=int(input("Ingrese su edad: "))
promedio=float(input("Ingrese su promedio general: "))
ingresos=float(input("Ingresos familiares mensuales: "))
if promedio>=6:
    if ingresos<300000:
        print("Beca completa")
    elif 300000<ingresos<600000:
        print("Media Beca")
    else:
        print("Rechazado")
else:
    print("Rechazado")

#Ejercicio_2
#Un hospital quiere organizar turnos según el tipo de paciente. El sistema debe pedir:
nombre_hospital=str(input("Nombre y Apellido: "))
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

#Ejercico_3
#Un banco necesita evaluar créditos personales.
nombre_banco=str(input("Nombre y Apellido: "))
cuit=input("Ingrese su CUIT (Ej: 20-99999999-5): ")
ingresos_mensuales=float(input("Ingrese sus ingresos mensuales: "))
antiguedad=int(input("Ingrese su antiguedad en años: "))
historial=str(input("Cual es tu historial crediticio: bueno / regular / malo "))

#if historial!="malo" and ingresos>=200000 and antiguedad>=2 :
#    if historial=="bueno":


#Condiciones:
#•	Si historial = malo → rechazo inmediato.
#•	Si ingresos < $200.000 → rechazo.
#•	Si ingresos ≥ $200.000 y antigüedad < 2 años → solo puede pedir hasta $500.000.
#•	Si ingresos ≥ $200.000 y antigüedad ≥ 2 años:
#o	Historial regular → hasta $1.000.000.
#o	Historial bueno → hasta $3.000.000.
