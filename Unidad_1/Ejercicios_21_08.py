#Ejercicio 6: Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. 
#Dicha calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

#p1=float(input("Ingresar calificación del primer parcial: "))
#p2=float(input("Ingresar calificación del segundo parcial: "))
#p3=float(input("Ingresar calificación del tercer parcial: "))
#exam_f=float(input("Ingresar calificación del Examen final: "))
#trab_f=float(input("Ingresar calificación del Trabajo final: "))
#prom_parciales=((p1+p2+p3)/3)
#calif_f=(prom_parciales*0.55)+(exam_f*0.3)+(trab_f*0.15)
#print(f"Su calificación final es: {calif_f}")

#Ejercicio 7: Conversión de divisas
#Un programa que lea un monto en dólares y lo convierta a pesos colombianos, 
#argentinos y euros usando tasas de cambio fijas definidas en el código.

#dolares=float(input("Ingrese el monto en dolares que desea cambiar: "))
#colom=dolares*4026.94
#arg=dolares*1359
#euro=dolares*0.86
#print(f"Pesos colombianos:{colom}")
#print(f"Pesos argentinos:{arg}")
#print(f"Euros:{euro}")

#Ejercicio 8: Viaje en auto
#Un auto consume 8 litros cada 100 km. 
#El usuario ingresa la distancia en km y el precio de la gasolina por litro.
#El programa debe calcular:
#cuántos litros se necesitan,
#cuánto costará el viaje,
#y cuántas horas tardará si la velocidad promedio es de 90 km/h.

dist=float(input("Ingrese la distacia a recorrer en km: "))
precio=float(input("Precio de la gasolina por litro: "))
litros_necesarios=dist*(8/100)
costo=precio*litros_necesarios
horas=dist*(1/90)
print(f"Si usted recorre {dist}km y la gasolina cuesta ${precio}")
print(f"Litros de gasolina necesarios: {litros_necesarios}")
print(f"Costo: ${costo}")
print(f"Horas de viaje: {horas} horas")

#Ejercicio 9: Préstamo bancario
#Un cliente solicita un préstamo que deberá pagar en 12 meses con interés fijo mensual del 2%.
#El usuario ingresa el monto solicitado, y el programa debe calcular:
#el monto total a devolver,
#el valor de cada cuota mensual.
