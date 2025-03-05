import matplotlib.pyplot as plt

print('Realizar gráfico de tarta')
cantidad_productos = 5
etiquetas = []
valores = []

for i in range(cantidad_productos):
    print(f'Introduzca el nombre del producto {i+1}:')
    etiqueta = input()
    etiquetas.append(etiqueta)
    print(f'Introduzca el precio del producto {i+1}:')
    valor = float(input())
    valores.append(valor)

plt.pie(valores, labels=etiquetas, autopct='%1.1f%%')
plt.title('Gráfico de tarta')
plt.savefig('images/tarta.png')
plt.show()