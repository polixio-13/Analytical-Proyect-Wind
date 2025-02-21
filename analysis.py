import matplotlib.pyplot as plt
import seaborn as sns
from database import df_combi, w_racha_combi, hr_combi, tm_mes_combi
from scipy.stats import linregress

#Mapa de dispersion para intentar detectar posibles tendencias o patrones con otras medidas
sns.pairplot(df_combi)
plt.show()

#Heatmap para sacar relaciones positivas o negativas rapidas entre otras medidas
corr_matrix= df_combi.corr()
sns.heatmap(corr_matrix, annot=True, cmap= "coolwarm")
plt.show()

#Grafico lineal de todos los años superpuestos para facil legibilidad
plt.figure(figsize=(12, 6))
for año, df_año in w_racha_combi.groupby('año'):
    plt.plot(df_año['mes'], df_año['w_racha'], marker='o', label=str(año))

plt.title('Comparación de la Velocidad del Viento en diferentes años')
plt.xlabel('Fecha')
plt.ylabel('Velocidad del Viento (w_racha)')
plt.legend(title='Año')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

#Grafico lineal de humedad relativa 
plt.figure(figsize=(12, 6))
for año, df_año in hr_combi.groupby('año'):
    plt.plot(df_año['mes'], df_año['hr'], marker='o', label=str(año))

plt.title('Comparación de la Humedad relativa en diferentes años')
plt.xlabel('Fecha')
plt.ylabel('Humedad relativa (hr)')
plt.legend(title='Año')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

#Grafico lineal tm superpuesto
plt.figure(figsize=(12, 6))
for año, df_año in tm_mes_combi.groupby('año'):
    plt.plot(df_año['mes'], df_año['tm_mes'], marker='o', label=str(año))

plt.title('Comparación de la temperatura media en diferentes años')
plt.xlabel('Fecha')
plt.ylabel('temperatura (tm_mes)')
plt.legend(title='Año')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# Ajuste de líneas de tendencia
años = df_combi['año'].unique()
promedio_viento = df_combi.groupby('año')['w_racha'].mean()
promedio_temp = df_combi.groupby('año')['tm_mes'].mean()

# Ajuste de regresión lineal para velocidad del viento
slope_viento, intercept_viento, r_value_viento, p_value_viento, std_err_viento = linregress(años, promedio_viento)

# Ajuste de regresión lineal para temperatura
slope_temp, intercept_temp, r_value_temp, p_value_temp, std_err_temp = linregress(años, promedio_temp)

# Visualizar la tendencia
plt.figure(figsize=(12, 6))

# Tendencia de la velocidad del viento
plt.subplot(2, 1, 1)
plt.plot(años, promedio_viento, marker='o', label='Promedio Anual Velocidad del Viento')
plt.plot(años, intercept_viento + slope_viento * años, 'r', label=f'Tendencia (slope={slope_viento:.2f})')
plt.title('Tendencia de la Velocidad del Viento')
plt.xlabel('Año')
plt.ylabel('Promedio Anual Velocidad del Viento')
plt.legend()

# Tendencia de la temperatura
plt.subplot(2, 1, 2)
plt.plot(años, promedio_temp, marker='o', label='Promedio Anual Temperatura')
plt.plot(años, intercept_temp + slope_temp * años, 'r', label=f'Tendencia (slope={slope_temp:.2f})')
plt.title('Tendencia de la Temperatura')
plt.xlabel('Año')
plt.ylabel('Promedio Anual Temperatura')
plt.legend()

plt.tight_layout()
plt.show()

# Mostrar resultados de la regresión lineal
print(f"Velocidad del Viento: slope={slope_viento:.2f}, p-value={p_value_viento:.3f}")
print(f"Temperatura: slope={slope_temp:.2f}, p-value={p_value_temp:.3f}")