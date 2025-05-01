import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors

#Arreglo de productividad semanal
produc_semanal = [75, 80, 90, 85, 70]

#Promedio y valor maximo
print("Promedio", np.mean(produc_semanal))
print("Valor máxima:", np.max(produc_semanal))

#Lectura del archivo CSV con Pandas
empleados = pd.read_csv(r"C:\tec\octavo\plyf\Tema4\empleados.csv", encoding='utf-8')

#Filtrar empleados del departamento Ventas
dep_ventas = empleados[empleados['Departamento'] == 'Ventas'][['Nombre', 'Departamento']]
print("\nEmpleados del departamento Ventas:\n", dep_ventas)

#Adicion de la columna Bono, la cual es el 10% del salario
salario = empleados['Salario'].to_numpy()
bono = salario * 0.10
empleados['Bono'] = bono
# Mostrar el DataFrame con la nueva columna
print("\nDatos de los empleados:\n", empleados)

#Grafico de barras con salario del empleado
plt.figure(figsize=(8, 6)) #Ajuste del tamano de la grafica para visualizar todos los datos
plt.bar(empleados['Nombre'], empleados['Salario'], color='green')
plt.title('Salario de cada empleado')
plt.xlabel('Nombre del empleado')
plt.ylabel('Salario del empleado')
plt.grid(axis='y')
plt.xticks(rotation=90) #Nombre rotado a 90 grados para visualizar nombres de manera correcta (posicion vertical)
plt.tight_layout() # Ajuste automatico de elementos para visualizar titulos y datos correctamente
plt.show()