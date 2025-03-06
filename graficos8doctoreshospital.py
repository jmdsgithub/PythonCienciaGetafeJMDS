import oracledb
import matplotlib.pyplot as plt

connection=oracledb.connect(user='system',password='oracle',dsn='localhost/XE')

print('Gráficos Doctores Hospital')

sql='select OFICIO, avg(SALARIO) as MEDIA from EMP group by OFICIO'

numero=[]
nombre=[]
cursor=connection.cursor()
cursor.execute(sql)
for numero, nombre in cursor:
    hospital.append(nombre)
    personas.append(numero)
cursor.close()
connection.close()

print(numero)
print(nombre)


plt.pie(numero, labels=nombre)
plt.title('Gráfico de media salarial EMP')
plt.show()