import matplotlib.pyplot as plt

diaSemana=[]
temperaturaDia=[]
print('Nombre del comercial')
for i in range(7):
    print('Nombre del dia de la semana')
    dia=input()
    print('Temperatura del dia')
    temp=int(input())
    diaSemana.append(dia)
    temperaturaDia.append(temp)
    

plt.plot(temperaturaDia, diaSemana)
plt.title('Gráfico de lineas')
plt.xlabel('Temperatura media')
plt.ylabel('Día de la semana')
plt.savefig('images/lineas.png')
plt.show()