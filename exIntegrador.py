teclados = []
pens = []
monto = 0
totales=[]

while monto < 1 or monto > 10**3:
    #determina el monto disponible
    monto = input('coloque el monto que desea: ')
    monto = int(monto)

    if monto >=1 and monto <= 10**3:
        pass
    else:
        print('Su monto no puede ser menor que 1 ni mayor que 1000')

tec = 0
dri = 0
while tec < 1 or tec >99 or dri < 1 or dri > 99:
    #determinaran la amplitud de la lista
    tec = int(input('coloque la cantidad de teclados: '))
    dri = int(input('coloque la cantidad de pen-drives: '))

    if tec >= 1 and tec <=99 and dri >= 1 and dri <= 99:
        pass
    else:
        print('usted no ha cumplido con los parametros de amplitud establecidos [1,99]')

#variables de los precios
tecPri = 0  
penPri = 0

#se rellena la lista de precios de los teclados
for i in range(tec):
    tecPri = 0
    while tecPri < 1 or tecPri > 10**3:
        tecPri = int(input(f'coloque los precios de los {tec} teclados: '))

        if tecPri >= 1 and tecPri <= 10**3:
            pass
        else:
            print('El precio no puede ser menor que 1 ni mayor que 1000')
    teclados.append(tecPri)


#ordena la lista de precios de los teclados de mayor a menor
teclados.sort(reverse=True)

#se rellena la lista de precios de los pendrives
for i in range(dri):
    penPri = 0
    while penPri < 1 or penPri > 10**3:
        penPri = int(input(f'coloque los precios de los {dri} pendrives: '))

        if penPri >= 1 and penPri <= 10**3:
            pass
        else:
            print('El precio no puede ser menor que 1 ni mayor que 1000')
    pens.append(penPri)


#ordena la lista de precios de los pendrives de mayor a menor
pens.sort(reverse=True)

print(teclados)
print(pens)

def obtenerMaximocosto(n,m,b):
    tmp=0
    tot=0

    #guarda en la lista 'totales' todos los resultados posibles
    for p in range(len(m)):
        for i in range(len(n)):
            tmp= m[p]+n[i]
            totales.append(tmp)
    totales.sort(reverse=True)
    print(totales)

    #evalua cual es el mayor costo sin sobre pasar el monto
    for i in range(len(totales)):
        if totales[i] <= monto:
            return totales[i]
        else:
            pass

print(obtenerMaximocosto(teclados,pens,monto))

    