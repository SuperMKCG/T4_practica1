import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors  # Importa el módulo de colores

# Creación de arreglos con numpy
# Arreglo de ventas por semana
ventas_semana = np.array([150, 200, 170, 220, 300, 250, 190])
print("Ventas por semana:", ventas_semana)

# Operaciones con arreglos
print("Promedio de ventas:", np.mean(ventas_semana))
print("Ventas máxima:", np.max(ventas_semana))
print("Ventas mínima:", np.min(ventas_semana))

# Lectura de archivos CSV con pandas
datos_ventas = pd.read_csv(r"C:\tec\octavo\plyf\Tema4\ventas.csv", encoding='utf-8')

# Operación con arreglos: Calcular ventas totales por producto
unidades = datos_ventas['Unidades Vendidas'].to_numpy()
precios = datos_ventas['Precio Unitario'].to_numpy()
ventas_totales = unidades * precios

# Agregar la columna de "Ventas Totales" al DataFrame
datos_ventas['Ventas Totales'] = ventas_totales

# Mostrar el DataFrame con la nueva columna
print("\nDatos de ventas:\n", datos_ventas)

# Visualización de datos con matplotlib
# Usar una paleta de colores predefinida para asignar colores
colores = plt.cm.tab20.colors

# Gráfica de pastel de Unidades vendidas por producto
plt.figure(figsize=(6, 6))
plt.pie(datos_ventas['Unidades Vendidas'], 
        labels=datos_ventas['Producto'],
        autopct='%1.1f%%',
        startangle=90,
        colors=colores[:len(datos_ventas)])  
plt.title('Unidades Vendidas por Producto')
plt.axis('equal')
plt.show()