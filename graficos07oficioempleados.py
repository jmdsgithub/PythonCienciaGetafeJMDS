import oracledb
import matplotlib.pyplot as plt

connection=oracledb.connect(user='system',password='oracle',dsn='localhost/XE')

print('Gráficos con BBDD')

sql='select OFICIO, avg(SALARIO) as MEDIA from EMP group by OFICIO'

oficios=[]
medias=[]
cursor=connection.cursor()
cursor.execute(sql)
for row in cursor:
    oficios.append(row[0])
    medias.append(row[1])
cursor.close()
connection.close()

print(oficios)
print(medias)


plt.pie(medias, labels=oficios)
plt.title('Gráfico de media salarial EMP')
plt.show()