import matplotlib.pyplot as plt

print('Realizar gráfico de tarta')
print('Introduzca la cantidad de productos a vender')
cantidad_productos=int(input())
print('Introduzca el nombre de cada producto')
etiquetas=input()
print('Introduzca el precio de cada producto')
valores=int(input())




etiquetas=['Betis','Atlético de Madrid','Barcelona','Real Madrid']

valores=[5,10,15,20]

plt.pie(valores, labels=etiquetas)
plt.title('Gráfico de tarta')
plt.savefig('images/tarta.png')
plt.show()