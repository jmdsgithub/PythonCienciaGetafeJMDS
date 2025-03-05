import matplotlib.pyplot as plt


productos=[]
ventas=[]
print('Nombre del comercial')
comercial=input()
for i in range(5):
    print('Nombre del producto')
    prod=input()
    print('Ventas del producto')
    num=int(input())
    productos.append(prod)
    ventas.append(num)

plt.pie(ventas, labels=productos)
plt.title(f'Comercial: {comercial}')
plt.savefig('images/tarta.png')
plt.show()